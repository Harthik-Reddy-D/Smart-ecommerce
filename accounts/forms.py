from django import forms
from django.contrib.auth import authenticate
from .models import User
class RegisterForm(forms.ModelForm):
 password=forms.CharField(widget=forms.PasswordInput,min_length=10); password_confirm=forms.CharField(widget=forms.PasswordInput)
 class Meta: model=User; fields=["name","email"]
 def clean(self):
  d=super().clean()
  if d.get("password")!=d.get("password_confirm"): raise forms.ValidationError("Passwords do not match")
  return d
 def save(self,commit=True):
  u=super().save(commit=False); u.set_password(self.cleaned_data["password"])
  if commit:u.save()
  return u
class LoginForm(forms.Form):
 email=forms.EmailField(); password=forms.CharField(widget=forms.PasswordInput)
 def clean(self):
  d=super().clean(); self.user=authenticate(email=d.get("email"),password=d.get("password"))
  if not self.user: raise forms.ValidationError("Invalid email or password")
  return d
