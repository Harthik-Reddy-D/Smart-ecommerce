from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,render
from .models import Order
@login_required
def history(request): return render(request,"orders/history.html",{"orders":Order.objects.filter(user=request.user).prefetch_related("items").order_by("-timestamp")})
@login_required
def detail(request,pk): return render(request,"orders/detail.html",{"order":get_object_or_404(Order.objects.prefetch_related("items"),pk=pk,user=request.user)})
