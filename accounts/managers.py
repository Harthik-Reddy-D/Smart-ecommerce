from django.contrib.auth.base_user import BaseUserManager
class UserManager(BaseUserManager):
 def create_user(self,email,password=None,**extra):
  if not email: raise ValueError("Email is required")
  user=self.model(email=self.normalize_email(email),**extra); user.set_password(password); user.save(using=self._db); return user
 def create_superuser(self,email,password=None,**extra):
  extra.setdefault("role",self.model.Role.ADMIN); extra.setdefault("is_staff",True); extra.setdefault("is_superuser",True); extra.setdefault("is_active",True)
  if not extra["is_staff"] or not extra["is_superuser"]: raise ValueError("Superuser must have staff and superuser flags")
  return self.create_user(email,password,**extra)
