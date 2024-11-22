from django.urls import path, include
from . import views
from . import models
from rest_framework import routers
from employee_app.views import *

router = routers.DefaultRouter()




router.register("Salesman_List", Salesman_ListView, basename="Salesman_List")
router.register("Salesmandetails", SalesmandetailsView, basename="Salesmandetails")
router.register("UndeliveredData", UndeliveredDataView, basename="UndeliveredData")
router.register("loginsalesmanwarehousedetails", loginsalesmanwarehousedetailsView, basename="loginsalesmanwarehousedetails")

router.register("invoice", SalesInvoiceDetailsView, basename="invoice")
router.register("invoicedetails", InvoiceDetailsView, basename="invociedetails")
router.register("Create_Dispatch", Create_DispatchView, basename="Create_Dispatch")


# router.register("Shopinfo", ShopinfoView, basename="Shopinf")

urlpatterns = [
    path("", include(router.urls)),
]
