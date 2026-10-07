import csv,io
from decimal import Decimal
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Sum,Count
from django.http import HttpResponse
from django.shortcuts import render
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from orders.models import Order,OrderItem
from products.models import Product
staff= lambda u:u.is_authenticated and u.is_staff_role
@user_passes_test(staff)
def index(request):
 paid=Order.objects.filter(payment_status=Order.PaymentStatus.PAID); total=paid.aggregate(v=Sum("total"))["v"] or Decimal("0"); top=OrderItem.objects.filter(order__payment_status=Order.PaymentStatus.PAID).values("product_name").annotate(q=Sum("quantity")).order_by("-q")[:10]; low=Product.objects.filter(stock__lte=5,is_active=True).order_by("stock")[:20]; trend=list(paid.values("timestamp__date").annotate(total=Sum("total")).order_by("timestamp__date")[30:]); return render(request,"dashboard/index.html",{"total":total,"orders":paid.count(),"top":top,"low":low,"trend":trend})
@user_passes_test(staff)
def csv_report(request):
 response=HttpResponse(content_type="text/csv"); response["Content-Disposition"]='attachment; filename="sales_report.csv"'; out=csv.writer(response); out.writerow(["Order","Customer","Total","Payment Status","Order Status","Timestamp"])
 for o in Order.objects.select_related("user").order_by("-timestamp"): out.writerow([o.id,o.user.email,o.total,o.payment_status,o.order_status,o.timestamp.isoformat()])
 return response
@user_passes_test(staff)
def pdf_report(request):
 response=HttpResponse(content_type="application/pdf"); response["Content-Disposition"]='attachment; filename="sales_report.pdf"'; p=canvas.Canvas(response,pagesize=A4); y=800; p.setFont("Helvetica-Bold",16); p.drawString(40,y,"Smart E-Commerce Sales Report"); y-=35; p.setFont("Helvetica",9)
 for o in Order.objects.select_related("user").order_by("-timestamp")[:45]:
  p.drawString(40,y,f"Order #{o.id} | {o.user.email[:28]} | INR {o.total} | {o.payment_status} | {o.order_status}"); y-=16
  if y<50:p.showPage(); y=800
 p.save(); return response
