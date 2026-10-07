from django.urls import path
from .views import detail,add,update,remove
from .api_views import CartListAPI,CartAddAPI,CartUpdateAPI,CartDeleteAPI
app_name="cart"
urlpatterns=[path("",detail,name="detail"),path("add/<int:product_id>/",add,name="add"),path("update/<int:item_id>/",update,name="update"),path("remove/<int:item_id>/",remove,name="remove"),path("api/",CartListAPI.as_view()),path("api/add/",CartAddAPI.as_view()),path("api/<int:pk>/",CartUpdateAPI.as_view()),path("api/<int:pk>/delete/",CartDeleteAPI.as_view())]
