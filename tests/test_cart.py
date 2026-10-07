import pytest
from rest_framework.test import APIClient
from cart.models import Cart
@pytest.mark.django_db
def test_add_cart(user,product):
 c=APIClient(); c.force_authenticate(user); r=c.post("/cart/api/add/",{"product_id":product.id,"quantity":2},format="json"); assert r.status_code==201; assert Cart.objects.get(user=user,product=product).quantity==2
@pytest.mark.django_db
def test_stock_validation(user,product):
 c=APIClient(); c.force_authenticate(user); r=c.post("/cart/api/add/",{"product_id":product.id,"quantity":99},format="json"); assert r.status_code==400
