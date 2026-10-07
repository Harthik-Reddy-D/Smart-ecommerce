from django.urls import path
from .views import home,detail
from .api_views import ProductListAPI,ProductDetailAPI
app_name="products"
urlpatterns=[path("",home,name="home"),path("product/<slug:slug>/",detail,name="detail"),path("api/",ProductListAPI.as_view(),name="api-list"),path("api/<int:pk>/",ProductDetailAPI.as_view(),name="api-detail")]
