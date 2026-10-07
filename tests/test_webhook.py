import pytest
from unittest.mock import patch
from django.test import Client
from accounts.models import User
from products.models import Category,Product
from orders.models import Order
@pytest.mark.django_db
def test_webhook_rejects_invalid_signature(settings):
 settings.STRIPE_WEBHOOK_SECRET="whsec_test"
 r=Client().post("/payments/webhook/",b"bad",content_type="application/json",HTTP_STRIPE_SIGNATURE="bad"); assert r.status_code==400
