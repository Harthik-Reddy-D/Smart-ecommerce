from django.db import migrations,models
import django.db.models.deletion
class Migration(migrations.Migration):
 initial=True
 dependencies=[("accounts","0001_initial")]
 operations=[migrations.CreateModel(name="Notification",fields=[("id",models.BigAutoField(primary_key=True,serialize=False)),("type",models.CharField(choices=[("order_confirmation","Order Confirmation"),("order_status","Order Status"),("payment_success","Payment Success"),("payment_failure","Payment Failure"),("shipping","Shipping")],max_length=40)),("message",models.TextField()),("is_read",models.BooleanField(default=False)),("timestamp",models.DateTimeField(auto_now_add=True)),("user",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="notifications",to="accounts.user"))],options={"indexes":[models.Index(fields=["user","is_read","-timestamp"],name="notificatio_user_id_0a71d3_idx")]})]
