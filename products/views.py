from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404,render
from .models import Category,Product

def home(request):
 qs=Product.objects.filter(is_active=True).select_related("category")
 q=request.GET.get("q","").strip(); category=request.GET.get("category",""); sort=request.GET.get("sort","-created_at"); min_price=request.GET.get("min_price"); max_price=request.GET.get("max_price")
 if q: qs=qs.filter(Q(name__icontains=q)|Q(description__icontains=q)|Q(category__name__icontains=q))
 if category: qs=qs.filter(category__slug=category)
 if min_price:
  try: qs=qs.filter(price__gte=min_price)
  except ValueError: pass
 if max_price:
  try: qs=qs.filter(price__lte=max_price)
  except ValueError: pass
 if sort in {"price","-price","popularity","-popularity","created_at","-created_at"}: qs=qs.order_by(sort)
 page=Paginator(qs,12).get_page(request.GET.get("page")); return render(request,"products/home.html",{"page":page,"categories":Category.objects.all(),"query":q})
def detail(request,slug): return render(request,"products/detail.html",{"product":get_object_or_404(Product.objects.select_related("category"),slug=slug,is_active=True)})
