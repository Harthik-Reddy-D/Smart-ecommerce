from .models import User
def create_social_user(strategy,details,response,*args,**kwargs):
 user=kwargs.get("user")
 if user:return {"user":user}
 email=(details.get("email") or response.get("email") or "").strip().lower()
 if not email:return {}
 user=User.objects.filter(email=email).first()
 if not user:
  name=details.get("fullname") or details.get("first_name") or response.get("name") or email.split("@")[0]
  user=User.objects.create_user(email=email,name=name)
 return {"user":user}
