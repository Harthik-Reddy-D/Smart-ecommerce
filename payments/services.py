import stripe
from django.conf import settings
from django.urls import reverse
from .models import Payment
stripe.api_key=settings.STRIPE_SECRET_KEY
def create_checkout_session(order,request):
 lines=[{"price_data":{"currency":"inr","product_data":{"name":i.product_name},"unit_amount":int(i.unit_price*100)},"quantity":i.quantity} for i in order.items.all()]
 session=stripe.checkout.Session.create(mode="payment",line_items=lines,client_reference_id=str(order.id),customer_email=order.user.email,success_url=settings.STRIPE_SUCCESS_URL+"?session_id={CHECKOUT_SESSION_ID}",cancel_url=settings.STRIPE_CANCEL_URL,metadata={"order_id":str(order.id)})
 order.stripe_session_id=session.id; order.save(update_fields=["stripe_session_id"]); Payment.objects.update_or_create(order=order,defaults={"amount":order.total,"payment_method":Payment.Method.STRIPE,"status":Payment.Status.PENDING}); return session
