from django.conf import settings
from django.db import models
class Order(models.Model):
 class PaymentStatus(models.TextChoices): PENDING="pending","Pending"; PAID="paid","Paid"; FAILED="failed","Failed"; REFUNDED="refunded","Refunded"
 class OrderStatus(models.TextChoices): PENDING="pending","Pending"; CONFIRMED="confirmed","Confirmed"; PROCESSING="processing","Processing"; SHIPPED="shipped","Shipped"; DELIVERED="delivered","Delivered"; CANCELLED="cancelled","Cancelled"
 user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,related_name="orders"); total=models.DecimalField(max_digits=12,decimal_places=2); payment_status=models.CharField(max_length=20,choices=PaymentStatus.choices,default=PaymentStatus.PENDING,db_index=True); order_status=models.CharField(max_length=20,choices=OrderStatus.choices,default=OrderStatus.PENDING,db_index=True); stripe_session_id=models.CharField(max_length=255,blank=True,null=True,unique=True); timestamp=models.DateTimeField(auto_now_add=True)
 class Meta: indexes=[models.Index(fields=["user","-timestamp"]),models.Index(fields=["payment_status","order_status"])]
 def __str__(self): return f"#{self.pk} {self.user.email}"
class OrderItem(models.Model):
 order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items"); product=models.ForeignKey("products.Product",on_delete=models.PROTECT); product_name=models.CharField(max_length=180); unit_price=models.DecimalField(max_digits=12,decimal_places=2); quantity=models.PositiveIntegerField()
 class Meta: constraints=[models.CheckConstraint(condition=models.Q(quantity__gt=0),name="order_item_quantity_gt_zero")]
 @property
 def subtotal(self): return self.unit_price*self.quantity
