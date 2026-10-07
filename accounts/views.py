from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from .forms import LoginForm,RegisterForm

def register(request):
 if request.user.is_authenticated:return redirect("products:home")
 form=RegisterForm(request.POST or None)
 if request.method=="POST" and form.is_valid(): login(request,form.save()); return redirect("products:home")
 return render(request,"accounts/register.html",{"form":form})
def login_view(request):
 if request.user.is_authenticated:return redirect("products:home")
 form=LoginForm(request.POST or None)
 if request.method=="POST" and form.is_valid(): login(request,form.user); return redirect(request.GET.get("next","/"))
 return render(request,"accounts/login.html",{"form":form})
@login_required
def logout_view(request): logout(request); messages.success(request,"Logged out successfully."); return redirect("products:home")
