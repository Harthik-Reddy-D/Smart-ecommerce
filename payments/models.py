from django.db import models
class Payment(models.Model):
 class Status(models.TextChoices): PENDING="pending","Pending"; SUCCEEDED="succeeded","Succeeded"; FAILED="failed","Failed"
 class Method(models.TextChoices): STRIPE="stripe","Stripe"
 order=models.OneToOneField("orders.Order",on_delete=models.PROTECT,related_name="payment"); amount=models.DecimalField(max_digits=12,decimal_places=2); payment_method=models.CharField(max_length=30,choices=Method.choices,default=Method.STRIPE); transaction_id=models.CharField(max_length=255,unique=True,null=True,blank=True); status=models.CharField(max_length=20,choices=Status.choices,default=Status.PENDING,db_index=True); created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)
 class Meta: indexes=[models.Index(fields=["status","created_at"])]
 def __str__(self): return f"Payment {self.order_id}"
class StripeEvent(models.Model):
 event_id=models.CharField(max_length=255,unique=True); event_type=models.CharField(max_length=100); processed_at=models.DateTimeField(auto_now_add=True)
