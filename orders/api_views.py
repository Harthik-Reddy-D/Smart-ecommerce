from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order, OrderItem
from .services import create_order_from_cart
from payments.services import create_checkout_session

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["id", "product_name", "unit_price", "quantity"]

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ["id", "total", "payment_status", "order_status", "timestamp", "items"]

class OrderListAPI(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related("items")

class OrderDetailAPI(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related("items")

class CheckoutAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        try:
            order = create_order_from_cart(request.user)
            session = create_checkout_session(order, request)
            return Response({"order_id": order.id, "checkout_url": session.url})
        except ValueError as exc:
            return Response({"detail": str(exc)}, status=400)
