from django.urls import path
from .views import index,csv_report,pdf_report
app_name="dashboard"
urlpatterns=[path("",index,name="index"),path("reports/sales.csv",csv_report,name="csv"),path("reports/sales.pdf",pdf_report,name="pdf")]
