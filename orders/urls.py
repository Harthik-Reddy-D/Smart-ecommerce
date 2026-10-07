from django.urls import path
from .views import history,detail
from .api_views import OrderListAPI,OrderDetailAPI,CheckoutAPI
app_name="orders"
urlpatterns=[path("",history,name="history"),path("<int:pk>/",detail,name="detail"),path("api/",OrderListAPI.as_view()),path("api/<int:pk>/",OrderDetailAPI.as_view()),path("api/checkout/",CheckoutAPI.as_view())]
