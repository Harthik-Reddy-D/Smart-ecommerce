from django.urls import path
from .api_views import RegisterAPI,LoginAPI,RefreshAPI,MeAPI,UserAdminAPI,UserAdminDetailAPI,StaffPingAPI
app_name="accounts_api"
urlpatterns=[path("register/",RegisterAPI.as_view()),path("token/",LoginAPI.as_view()),path("token/refresh/",RefreshAPI.as_view()),path("me/",MeAPI.as_view()),path("users/",UserAdminAPI.as_view()),path("users/<int:pk>/",UserAdminDetailAPI.as_view()),path("staff-ping/",StaffPingAPI.as_view())]
