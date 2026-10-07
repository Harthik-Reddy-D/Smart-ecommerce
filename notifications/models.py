from django.conf import settings
from django.db import models
class Notification(models.Model):
 class Type(models.TextChoices): ORDER_CONFIRMATION="order_confirmation","Order Confirmation"; ORDER_STATUS="order_status","Order Status"; PAYMENT_SUCCESS="payment_success","Payment Success"; PAYMENT_FAILURE="payment_failure","Payment Failure"; SHIPPING="shipping","Shipping"
 user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="notifications");order = models.ForeignKey(
    "orders.Order",
    on_delete=models.CASCADE,
    null=True,
    blank=True,
    related_name="notifications",
)
 type=models.CharField(max_length=40,choices=Type.choices); 
 message=models.TextField();
 is_read=models.BooleanField(default=False); timestamp=models.DateTimeField(auto_now_add=True)
class Meta: indexes=[models.Index(fields=["user","is_read","-timestamp"])]
