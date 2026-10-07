import pytest
from accounts.models import User
from products.models import Category,Product
@pytest.fixture
def user(db): return User.objects.create_user(email="user@example.com",password="StrongPass123!",name="Test User")
@pytest.fixture
def staff(db): return User.objects.create_user(email="staff@example.com",password="StrongPass123!",name="Staff",role=User.Role.STAFF,is_staff=True)
@pytest.fixture
def product(db):
 c=Category.objects.create(name="Books",slug="books"); return Product.objects.create(name="Django Book",slug="django-book",description="Learn Django",price="1000.00",stock=10,category=c)
