from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db import models
from .managers import UserManager
class User(AbstractBaseUser,PermissionsMixin):
 class Role(models.TextChoices): ADMIN="admin","Admin"; STAFF="staff","Staff"; CUSTOMER="customer","Customer"
 id=models.BigAutoField(primary_key=True); name=models.CharField(max_length=120); email=models.EmailField(unique=True); role=models.CharField(max_length=20,choices=Role.choices,default=Role.CUSTOMER,db_index=True); is_active=models.BooleanField(default=True); is_staff=models.BooleanField(default=False); date_joined=models.DateTimeField(auto_now_add=True)
 USERNAME_FIELD="email"; REQUIRED_FIELDS=["name"]
 objects=UserManager()
 class Meta: indexes=[models.Index(fields=["role"]),models.Index(fields=["email"])]
 def __str__(self): return self.email
 @property
 def is_admin(self): return self.role==self.Role.ADMIN
 @property
 def is_staff_role(self): return self.role in {self.Role.ADMIN,self.Role.STAFF}
