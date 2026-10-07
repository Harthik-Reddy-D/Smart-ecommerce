from rest_framework import generics,filters,permissions
from .models import Product
from .serializers import ProductSerializer
from accounts.permissions import IsStaffOrAdmin
class ProductListAPI(generics.ListCreateAPIView):
 queryset=Product.objects.filter(is_active=True).select_related("category"); serializer_class=ProductSerializer; filter_backends=[filters.SearchFilter,filters.OrderingFilter]; search_fields=["name","description","category__name"]; ordering_fields=["price","popularity","created_at"]; permission_classes=[permissions.IsAuthenticatedOrReadOnly]
 def get_permissions(self): return [IsStaffOrAdmin()] if self.request.method=="POST" else [permissions.AllowAny()]
class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
 queryset=Product.objects.all(); serializer_class=ProductSerializer
 def get_permissions(self): return [IsStaffOrAdmin()] if self.request.method in {"PUT","PATCH","DELETE"} else [permissions.AllowAny()]
