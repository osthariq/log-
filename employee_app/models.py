import json
from django.db import models



class Salesman_List(models.Model):

    SALESREP_ID=  models.CharField(max_length=200, default="")
    SALESMAN_NO=  models.CharField(max_length=200, default="")
    SALESMAN_NAME=  models.CharField(max_length=200, default="")

    class Meta:
        db_table = "SALESMAN_LIST"
        ordering = ["id"] 

class Create_DispatchModels(models.Model):
   
    REQ_ID=  models.CharField(max_length=200, default="")
    TO_WAREHOUSE=  models.CharField(max_length=200, default="")
    ORG_ID=  models.CharField(max_length=200, default="")
    ORG_NAME=  models.CharField(max_length=200, default="")
    SALESREP_ID=  models.CharField(max_length=200, default="")
    SALESMAN_NO=  models.CharField(max_length=200, default="")
    SALESMAN_NAME=  models.CharField(max_length=200, default="")
    SALES_CHANNEL=  models.CharField(max_length=200, default="")
    CUSTOMER_ID=  models.CharField(max_length=200, default="")
    CUSTOMER_NUMBER=  models.CharField(max_length=200, default="")
    CUSTOMER_NAME=  models.CharField(max_length=200, default="")
    CUSTOMER_SITE_ID=  models.CharField(max_length=200, default="")
    INVOICE_DATE=  models.DateTimeField(max_length=200, default="")
    INVOICE_NUMBER=  models.CharField(max_length=200, default="")
    LINE_NUMBER=  models.CharField(max_length=200, default="")
    INVENTORY_ITEM_ID=  models.CharField(max_length=200, default="")
    TOT_QUANTITY=  models.CharField(max_length=200, default="")
    DISPATCHED_QTY=  models.CharField(max_length=200, default="")
    BALANCE_QTY=  models.CharField(max_length=200, default="")
    AMOUNT=  models.CharField(max_length=200, default="")
    ITEM_COST=  models.CharField(max_length=200, default="")
   

    class Meta:
        db_table = "CREATE_DISPATCH"
        ordering = ["id"] 


