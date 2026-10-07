import pytest
from rest_framework.test import APIClient
@pytest.mark.django_db
def test_staff_endpoint_denied_to_customer(user):
 c=APIClient(); c.force_authenticate(user); assert c.get("/api/accounts/staff-ping/").status_code==403
@pytest.mark.django_db
def test_staff_endpoint_allowed(staff):
 c=APIClient(); c.force_authenticate(staff); assert c.get("/api/accounts/staff-ping/").status_code==200
