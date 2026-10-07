from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from .models import Notification
@login_required
def index(request): return render(request,"notifications/index.html",{"notifications":request.user.notifications.all()[:100]})
@login_required
def read(request,pk): Notification.objects.filter(id=pk,user=request.user).update(is_read=True); return redirect("notifications:index")
