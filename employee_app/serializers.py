from rest_framework import serializers

from .models import *

class UndeliveredDataSerializer(serializers.Serializer):
    undel_id = serializers.IntegerField()
    to_warehouse = serializers.CharField(max_length=100)
    org_id = serializers.CharField(max_length=200)  # Change to CharField
    org_name = serializers.CharField(max_length=255)
    salesrep_id = serializers.CharField(max_length=200)  # Change to CharField
    salesman_no = serializers.CharField(max_length=50)
    salesman_name = serializers.CharField(max_length=255)
    customer_id = serializers.CharField(max_length=200)  # Change to CharField
    customer_number = serializers.CharField(max_length=50)
    customer_name = serializers.CharField(max_length=255)
    sales_channel = serializers.CharField(max_length=100)
    customer_site_id = serializers.CharField(max_length=200)  # Change to CharField
    cus_location = serializers.CharField(max_length=255)
    customer_trx_id = serializers.CharField(max_length=200)  # Change to CharField
    customer_trx_line_id = serializers.CharField(max_length=200)  # Change to CharField
    invoice_date = serializers.DateTimeField()
    invoice_number = serializers.CharField(max_length=50)
    line_number = serializers.IntegerField()
    inventory_item_id = serializers.CharField(max_length=200)  # Change to CharField
    quantity = serializers.DecimalField(max_digits=10, decimal_places=2)
    dispatch_qty = serializers.DecimalField(max_digits=10, decimal_places=2)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    item_cost = serializers.DecimalField(max_digits=10, decimal_places=2)
    flag = serializers.CharField(max_length=10)
    reference1 = serializers.CharField(max_length=255)
    reference2 = serializers.CharField(max_length=255)
    attribute1 = serializers.CharField(max_length=255)
    attribute2 = serializers.CharField(max_length=255)
    attribute3 = serializers.CharField(max_length=255)
    attribute4 = serializers.CharField(max_length=255)
    attribute5 = serializers.CharField(max_length=255)
    freeze_status = serializers.CharField(max_length=50)
    last_update_date = serializers.DateTimeField()
    last_updated_by = serializers.CharField(max_length=200)  # Change to CharField
    creation_date = serializers.DateTimeField()
    created_by = serializers.CharField(max_length=200)  # Change to CharField
    last_update_login = serializers.CharField(max_length=200)  # Change to CharField
    warehouse_id = serializers.CharField(max_length=200)  # Change to CharField
    warehouse_name = serializers.CharField(max_length=255)
    legacy_ref = serializers.CharField(max_length=255)
    inv_row_id = serializers.CharField(max_length=200)  # Change to CharField


class SalesmanDataSerializer(serializers.Serializer):
    salesrep_id = serializers.CharField(max_length=200)  # Change to CharField
    salesman_no = serializers.CharField(max_length=50)
    salesman_name = serializers.CharField(max_length=255)

class loginsalesmanwarehousedetailsSerializer(serializers.Serializer):
    salesrep_id = serializers.CharField(max_length=200)  # Change to CharField
    salesman_no = serializers.CharField(max_length=50)
    salesman_name = serializers.CharField(max_length=255)
    
    salesman_channel = serializers.CharField(max_length=255)
    to_warehouse = serializers.CharField()
    org_id = serializers.CharField()
    org_name = serializers.CharField()
    customer_id = serializers.IntegerField()
    customer_number = serializers.CharField()
    customer_name = serializers.CharField()
    customer_site_id = serializers.CharField(max_length=200)
    customer_site_channel  = serializers.CharField()
    
class SalesmanInvoicedetailsSerializer(serializers.Serializer):

    invoice_number = serializers.CharField(max_length=50)

class invoicedetailsSerializer(serializers.Serializer):
    invoice_number = serializers.CharField(max_length=20)
    line_number = serializers.IntegerField()
    inventory_item_id = serializers.CharField(max_length=50)
    quantity = serializers.FloatField()
    dispatch_qty = serializers.FloatField()
    amount = serializers.FloatField()
    item_cost = serializers.FloatField()


class create_Dispatchserializers(serializers.ModelSerializer):
    class Meta:
        model = Create_DispatchModels
        fields = "__all__"

class Salesman_Listserializers(serializers.ModelSerializer):
    class Meta:
        model = Salesman_List
        fields = "__all__"