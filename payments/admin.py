from django.contrib import admin
from .models import Payment,StripeEvent
admin.site.register(Payment); admin.site.register(StripeEvent)
