from decimal import Decimal
from django.db import transaction
from cart.models import Cart
from .models import Order,OrderItem
@transaction.atomic
def create_order_from_cart(user):
 items=list(Cart.objects.select_for_update().select_related("product").filter(user=user))
 if not items: raise ValueError("Cart is empty")
 total=Decimal("0")
 for item in items:
  if not item.product.is_active or item.quantity>item.product.stock: raise ValueError(f"Insufficient stock for {item.product.name}")
  total+=item.product.price*item.quantity
 order=Order.objects.create(user=user,total=total)
 for item in items:
  product=item.product; product.stock-=item.quantity; product.popularity+=item.quantity; product.save(update_fields=["stock","popularity","updated_at"])
  OrderItem.objects.create(order=order,product=product,product_name=product.name,unit_price=product.price,quantity=item.quantity)
 Cart.objects.filter(user=user).delete()
 from notifications.services import create_notification
 create_notification(user,"order_confirmation",f"Order #{order.id} was created and is awaiting payment.",order=order)
 return order
