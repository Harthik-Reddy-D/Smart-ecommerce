from django.urls import path
from .views import checkout,success,cancel,webhook
app_name="payments"
urlpatterns=[path("checkout/",checkout,name="checkout"),path("success/",success,name="success"),path("cancel/",cancel,name="cancel"),path("webhook/",webhook,name="webhook")]
