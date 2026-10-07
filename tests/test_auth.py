import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from accounts.models import User
@pytest.mark.django_db
def test_register_api():
 r=APIClient().post("/api/accounts/register/",{"name":"New User","email":"new@example.com","password":"StrongPass123!"},format="json"); assert r.status_code==201; assert User.objects.filter(email="new@example.com").exists()
@pytest.mark.django_db
def test_jwt_login(user):
 r=APIClient().post("/api/accounts/token/",{"email":"user@example.com","password":"StrongPass123!"},format="json"); assert r.status_code==200; assert "access" in r.data
