from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User
class UserSerializer(serializers.ModelSerializer):
 class Meta: model=User; fields=["id","name","email","role","date_joined"]
class RegisterSerializer(serializers.ModelSerializer):
 password=serializers.CharField(write_only=True,min_length=10)
 class Meta: model=User; fields=["name","email","password"]
 def create(self,validated): return User.objects.create_user(**validated)
class RoleSerializer(serializers.ModelSerializer):
 class Meta: model=User; fields=["id","name","email","role","is_active"]
class EmailTokenSerializer(TokenObtainPairSerializer):
 username_field="email"
 @classmethod
 def get_token(cls,user):
  token=super().get_token(user); token["role"]=user.role; token["email"]=user.email; return token
