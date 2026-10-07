import pytest
from cart.models import Cart
from orders.services import create_order_from_cart
from orders.models import Order
@pytest.mark.django_db
def test_checkout_creates_order_and_decrements_stock(user,product):
 Cart.objects.create(user=user,product=product,quantity=3); o=create_order_from_cart(user); product.refresh_from_db(); assert o.total==3000; assert product.stock==7; assert not Cart.objects.filter(user=user).exists()
