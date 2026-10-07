from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("product_name", "unit_price", "quantity")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "total", "payment_status", "order_status", "timestamp")
    list_filter = ("payment_status", "order_status")
    search_fields = ("user__email",)
    inlines = [OrderItemInline]
    def save_model(self, request, obj, form, change):
        old = None
        if change:
            old = Order.objects.get(pk=obj.pk).order_status
        super().save_model(request, obj, form, change)
        if change and old != obj.order_status:
            from notifications.services import notify_order_status
            notify_order_status(obj, old)
