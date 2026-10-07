import logging
import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,redirect,render
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order
from orders.services import create_order_from_cart
from .models import Payment,StripeEvent
from .services import create_checkout_session
logger=logging.getLogger("smartshop")
@login_required
def checkout(request):
 try: order=create_order_from_cart(request.user); session=create_checkout_session(order,request); return redirect(session.url,permanent=False)
 except ValueError as e: return render(request,"cart/detail.html",{"items":request.user.cart_items.select_related("product"),"error":str(e)})
def success(request): return render(request,"payments/result.html",{"success":True})
def cancel(request): return render(request,"payments/result.html",{"success":False})
@csrf_exempt
def webhook(request):
    payload = request.body
    sig = request.META.get("HTTP_STRIPE_SIGNATURE", "")

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig,
            settings.STRIPE_WEBHOOK_SECRET,
        )
    except (ValueError, stripe.error.SignatureVerificationError):
        return HttpResponse(status=400)

    with transaction.atomic():
        if StripeEvent.objects.filter(event_id=event["id"]).exists():
            return HttpResponse(status=200)

        obj = event["data"]["object"].to_dict()
        et = event["type"]
        metadata = obj.get("metadata") or {}
        order_id = metadata.get("order_id")

        if order_id:
            order = Order.objects.select_for_update().filter(id=order_id).first()
            if order:
                payment, _ = Payment.objects.select_for_update().get_or_create(
                    order=order,
                    defaults={"amount": order.total},
                )

                if et == "checkout.session.completed":
                    payment.status = Payment.Status.SUCCEEDED
                    payment.transaction_id = obj.get("payment_intent") or obj.get("id")
                    order.payment_status = Order.PaymentStatus.PAID
                    order.order_status = Order.OrderStatus.CONFIRMED
                    payment.save()
                    order.save(update_fields=["payment_status", "order_status"])
                    from notifications.services import create_notification
                    create_notification(order.user, "payment_success", f"Payment received for order #{order.id}.",order=order)
                elif et in {"checkout.session.async_payment_failed", "checkout.session.expired"}:
                    payment.status = Payment.Status.FAILED
                    payment.transaction_id = obj.get("payment_intent") or obj.get("id")
                    order.payment_status = Order.PaymentStatus.FAILED
                    from products.models import Product
                    for item in order.items.select_related("product"):
                        Product.objects.filter(pk=item.product_id).update(
                            stock=__import__("django.db.models", fromlist=["F"]).F("stock") + item.quantity
                        )
                    payment.save()
                    order.save(update_fields=["payment_status"])
                    from notifications.services import create_notification
                    create_notification(order.user, "payment_failure", f"Payment failed for order #{order.id}.", order=order)

        StripeEvent.objects.create(event_id=event["id"], event_type=et)

    return HttpResponse(status=200) 