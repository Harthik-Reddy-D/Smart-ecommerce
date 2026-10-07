from django.db import transaction
from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cart
from products.models import Product

class CartSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    price = serializers.DecimalField(source="product.price", max_digits=12, decimal_places=2, read_only=True)
    subtotal = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    class Meta:
        model = Cart
        fields = ["id", "product", "product_name", "price", "quantity", "subtotal"]

class CartListAPI(generics.ListAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user).select_related("product")

class CartAddAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        p = Product.objects.filter(id=request.data.get("product_id"), is_active=True).first()
        if not p:
            return Response({"detail": "Product not found"}, status=404)
        try:
            qty = int(request.data.get("quantity", 1))
        except (TypeError, ValueError):
            return Response({"detail": "Invalid quantity"}, status=400)
        if qty < 1:
            return Response({"detail": "Invalid quantity"}, status=400)
        with transaction.atomic():
            item = Cart.objects.select_for_update().filter(user=request.user, product=p).first()
            new = (item.quantity if item else 0) + qty
            if new > p.stock:
                return Response({"detail": "Insufficient stock"}, status=400)
            if item:
                item.quantity = new
                item.save(update_fields=["quantity", "updated_at"])
            else:
                item = Cart.objects.create(user=request.user, product=p, quantity=qty)
        return Response(CartSerializer(item).data, status=201)

class CartUpdateAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def patch(self, request, pk):
        item = Cart.objects.filter(id=pk, user=request.user).select_related("product").first()
        if not item:
            return Response({"detail": "Not found"}, status=404)
        try:
            qty = int(request.data.get("quantity", 0))
        except (TypeError, ValueError):
            return Response({"detail": "Invalid quantity"}, status=400)
        if qty < 1 or qty > item.product.stock:
            return Response({"detail": "Invalid quantity"}, status=400)
        item.quantity = qty
        item.save(update_fields=["quantity", "updated_at"])
        return Response(CartSerializer(item).data)

class CartDeleteAPI(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
