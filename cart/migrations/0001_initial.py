from django.db import migrations,models
import django.db.models.deletion
class Migration(migrations.Migration):
 initial=True
 dependencies=[("accounts","0001_initial"),("products","0001_initial")]
 operations=[migrations.CreateModel(name="Cart",fields=[("id",models.BigAutoField(primary_key=True,serialize=False)),("quantity",models.PositiveIntegerField(default=1)),("updated_at",models.DateTimeField(auto_now=True)),("product",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="cart_items",to="products.product")),("user",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="cart_items",to="accounts.user"))],options={"constraints":[models.UniqueConstraint(fields=("user","product"),name="unique_cart_user_product")],"indexes":[models.Index(fields=["user","updated_at"],name="cart_cart_user_1f5b6a_idx")]})]
