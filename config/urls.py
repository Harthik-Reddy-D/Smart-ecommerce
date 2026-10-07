from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include,path
from django.http import JsonResponse
def health(request): return JsonResponse({"status":"ok","service":"smart-ecommerce"})
urlpatterns=[path("admin/",admin.site.urls),path("health/",health),path("accounts/",include("accounts.urls")),path("api/accounts/",include("accounts.api_urls")),path("",include("products.urls")),path("cart/",include("cart.urls")),path("orders/",include("orders.urls")),path("payments/",include("payments.urls")),path("notifications/",include("notifications.urls")),path("dashboard/",include("dashboard.urls")),path("oauth/",include("social_django.urls",namespace="social"))]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
