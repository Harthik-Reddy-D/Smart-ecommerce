from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404,redirect,render
from products.models import Product
from .forms import QuantityForm
from .models import Cart
@login_required
def detail(request):
 items=Cart.objects.filter(user=request.user).select_related("product"); return render(request,"cart/detail.html",{"items":items,"total":sum(x.subtotal for x in items)})
@login_required
def add(request,product_id):
 product=get_object_or_404(Product,id=product_id,is_active=True)
 with transaction.atomic():
  item,created=Cart.objects.select_for_update().get_or_create(user=request.user,product=product)
  qty=item.quantity+1 if not created else 1
  if qty>product.stock: messages.error(request,"Requested quantity exceeds available stock."); return redirect("products:detail",product.slug)
  item.quantity=qty; item.save(update_fields=["quantity","updated_at"])
 messages.success(request,"Product added to cart."); return redirect("cart:detail")
@login_required
def update(request,item_id):
 item=get_object_or_404(Cart.objects.select_related("product"),id=item_id,user=request.user); form=QuantityForm(request.POST)
 if form.is_valid() and form.cleaned_data["quantity"]<=item.product.stock: item.quantity=form.cleaned_data["quantity"]; item.save(update_fields=["quantity","updated_at"])
 else: messages.error(request,"Invalid quantity or insufficient stock.")
 return redirect("cart:detail")
@login_required
def remove(request,item_id): Cart.objects.filter(id=item_id,user=request.user).delete(); return redirect("cart:detail")
