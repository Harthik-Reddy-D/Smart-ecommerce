from django.urls import path
from .views import index,read
app_name="notifications"
urlpatterns=[path("",index,name="index"),path("read/<int:pk>/",read,name="read")]
