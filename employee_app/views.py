from django.db.models import Sum
from rest_framework.decorators import action

from rest_framework.response import Response
from django.db import connection
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .serializers import *

class StandardResultsSetPagination(PageNumberPagination):
    """
    Custom pagination class to define default page size and maximum page size.
    """
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100
    

class UndeliveredDataView(viewsets.ViewSet):
    """
    A ViewSet for listing undelivered data using a custom SQL query.
    """
    pagination_class = StandardResultsSetPagination

    def list(self, request):
        # Get the salesman_no parameter from the request
        salesman_no = request.query_params.get('salesman_no', None)

        # Prepare the SQL query
        query = '''
            SELECT * FROM BUYP.BUYP.XXALJE_UNDELIVERED_DATA_BUYP1
        '''

        # Add a WHERE clause if salesman_no is provided
        if salesman_no:
            query += ' WHERE SALESMAN_NO = %s'
        
        # Execute raw SQL query
        with connection.cursor() as cursor:
            if salesman_no:
                cursor.execute(query, [salesman_no])  # Use parameterized query for safety
            else:
                cursor.execute(query)
                
            rows = cursor.fetchall()

        # Prepare the data for serialization
        data = [
            {
                'undel_id': row[0],
                'to_warehouse': row[1],
                'org_id': row[2],
                'org_name': row[3],
                'salesrep_id': row[4],
                'salesman_no': row[5],
                'salesman_name': row[6],
                'customer_id': row[7],
                'customer_number': row[8],
                'customer_name': row[9],
                'sales_channel': row[10],
                'customer_site_id': row[11],
                'cus_location': row[12],
                'customer_trx_id': row[13],
                'customer_trx_line_id': row[14],
                'invoice_date': row[15],
                'invoice_number': row[16],
                'line_number': row[17],
                'inventory_item_id': row[18],
                'quantity': row[19],
                'dispatch_qty': row[20],
                'amount': row[21],
                'item_cost': row[22],
                'flag': row[23],
                'reference1': row[24],
                'reference2': row[25],
                'attribute1': row[26],
                'attribute2': row[27],
                'attribute3': row[28],
                'attribute4': row[29],
                'attribute5': row[30],
                'freeze_status': row[31],
                'last_update_date': row[32],
                'last_updated_by': row[33],
                'creation_date': row[34],
                'created_by': row[35],
                'last_update_login': row[36],
                'warehouse_id': row[37],
                'warehouse_name': row[38],
                'legacy_ref': row[39],
                'inv_row_id': row[40]
            } for row in rows
        ]

        # Paginate the data
        paginator = StandardResultsSetPagination()
        paginated_data = paginator.paginate_queryset(data, request)

        # Serialize the paginated data
        serializer = UndeliveredDataSerializer(paginated_data, many=True)

        # Return the paginated response
        return paginator.get_paginated_response(serializer.data)

class SalesmandetailsView(viewsets.ViewSet):
    """
    A ViewSet for listing distinct salesman data.
    """
    pagination_class = StandardResultsSetPagination

    def list(self, request):
        # Prepare the SQL query to get distinct salesman data
        query = '''
            SELECT DISTINCT SALESMAN_NO, SALESREP_ID, SALESMAN_NAME
            FROM BUYP.XXALJE_UNDELIVERED_DATA_BUYP1
        '''

        # Execute raw SQL query
        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()

        # Prepare the data for serialization
        data = [
            {
                'salesman_no': row[0],
                'salesrep_id': row[1],
                'salesman_name': row[2],
            } for row in rows
        ]

        # Paginate the data
        paginator = StandardResultsSetPagination()
        paginated_data = paginator.paginate_queryset(data, request)

        # Serialize the paginated data
        serializer = SalesmanDataSerializer(paginated_data, many=True)  # Use correct serializer

        # Return the paginated response
        return paginator.get_paginated_response(serializer.data)
    
class loginsalesmanwarehousedetailsView(viewsets.ViewSet):
    """
    A ViewSet for listing undelivered data using a custom SQL query.
    """
    pagination_class = StandardResultsSetPagination

    def list(self, request):
        # Get the salesman_no parameter from the request
        salesman_no = request.query_params.get('salesman_no', None)

        # Prepare the base SQL query, selecting only the necessary fields
        query = '''
            SELECT DISTINCT 
                SALESREP_ID,
                SALESMAN_NO,
                SALESMAN_NAME,
                SALES_CHANNEL,
                TO_WAREHOUSE, 
                ORG_ID,
                ORG_NAME,
                CUSTOMER_ID, 
                CUSTOMER_NUMBER, 
                CUSTOMER_NAME ,CUSTOMER_SITE_ID,SALES_CHANNEL
            FROM BUYP.BUYP.XXALJE_UNDELIVERED_DATA_BUYP1
        '''

        # Add a WHERE clause if salesman_no is provided
        if salesman_no:
            query += ' WHERE SALESMAN_NO = %s'

        # Execute the raw SQL query
        with connection.cursor() as cursor:
            if salesman_no:
                cursor.execute(query, [salesman_no])  # Use parameterized query for safety
            else:
                cursor.execute(query)
                
            rows = cursor.fetchall()

        # Prepare the data for serialization
        data = [
            { 
                'salesrep_id': row[0],
                'salesman_no': row[1],
                'salesman_name': row[2],                
                'salesman_channel': row[3],
                'to_warehouse': row[4],
                'org_id': row[5],
                'org_name': row[6],

                'customer_id': row[7],
                'customer_number': row[8],
                'customer_name': row[9],                
                'customer_site_id': row[10],              
                'customer_site_channel': row[11],
            } for row in rows
        ]

        # Paginate the data
        paginator = StandardResultsSetPagination()
        paginated_data = paginator.paginate_queryset(data, request)

        # Serialize the paginated data
        serializer = loginsalesmanwarehousedetailsSerializer(paginated_data, many=True)

        # Return the paginated response
        return paginator.get_paginated_response(serializer.data)

class SalesInvoiceDetailsView(viewsets.ViewSet):
    """
    A ViewSet for listing invoices filtered by salesman_no and customer_number.
    """
    pagination_class = StandardResultsSetPagination

    def list(self, request):
        # Get the salesman_no and customer_number parameters from the request
        salesman_no = request.query_params.get('salesman_no', None)
        customer_number = request.query_params.get('customer_number', None)

        # Prepare the base SQL query to select salesman_no, customer_number, and invoice_number
        query = '''
            SELECT SALESMAN_NO, CUSTOMER_NUMBER, INVOICE_NUMBER
            FROM BUYP.[XXALJE_UNDELIVERED_DATA_BUYP1]
        '''

        # Add a WHERE clause if salesman_no and customer_number are provided
        conditions = []
        params = []

        if salesman_no:
            conditions.append('SALESMAN_NO = %s')
            params.append(salesman_no)
        if customer_number:
            conditions.append('CUSTOMER_NUMBER = %s')
            params.append(customer_number)

        # Join conditions with AND if both parameters are provided
        if conditions:
            query += ' WHERE ' + ' AND '.join(conditions)

        # Execute the raw SQL query
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            rows = cursor.fetchall()

        # Prepare the data for serialization (displaying salesman_no, customer_number, and invoice_number)
        data = [{'salesman_no': row[0], 'customer_number': row[1], 'invoice_number': row[2]} for row in rows]

        # Paginate the data
        paginator = StandardResultsSetPagination()
        paginated_data = paginator.paginate_queryset(data, request)

        # Serialize the paginated data
        serializer = SalesmanInvoicedetailsSerializer(paginated_data, many=True)

        # Return the paginated response
        return paginator.get_paginated_response(serializer.data)

class InvoiceDetailsView(viewsets.ViewSet):
    """
    A ViewSet for listing invoice details filtered by salesman_no, customer_number, and invoice_number.
    """
    pagination_class = StandardResultsSetPagination

    def list(self, request):
        # Get the salesman_no, customer_number, and invoice_number parameters from the request
        salesman_no = request.query_params.get('salesman_no', None)
        customer_number = request.query_params.get('customer_number', None)
        invoice_number = request.query_params.get('invoice_number', None)

        # Prepare the base SQL query to select the required columns
        query = '''
            SELECT INVOICE_NUMBER, LINE_NUMBER, INVENTORY_ITEM_ID, QUANTITY, DISPATCH_QTY, AMOUNT, ITEM_COST
            FROM BUYP.[XXALJE_UNDELIVERED_DATA_BUYP1]
        '''

        # Add a WHERE clause if salesman_no, customer_number, or invoice_number are provided
        conditions = []
        params = []

        if salesman_no:
            conditions.append('SALESMAN_NO = %s')
            params.append(salesman_no)
        if customer_number:
            conditions.append('CUSTOMER_NUMBER = %s')
            params.append(customer_number)
        if invoice_number:
            conditions.append('INVOICE_NUMBER = %s')
            params.append(invoice_number)

        # Join conditions with AND if any parameters are provided
        if conditions:
            query += ' WHERE ' + ' AND '.join(conditions)

        # Execute the raw SQL query
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            rows = cursor.fetchall()

        # Prepare the data for serialization
        data = [
            {
                'invoice_number': row[0],
                'line_number': row[1],
                'inventory_item_id': row[2],
                'quantity': row[3],
                'dispatch_qty': row[4],
                'amount': row[5],
                'item_cost': row[6]
            }
            for row in rows
        ]

        # Paginate the data
        paginator = StandardResultsSetPagination()
        paginated_data = paginator.paginate_queryset(data, request)

        # Serialize the paginated data
        serializer = invoicedetailsSerializer(paginated_data, many=True)

        # Return the paginated response
        return paginator.get_paginated_response(serializer.data)
    

class Create_DispatchView(viewsets.ModelViewSet):
    queryset = Create_DispatchModels.objects.all()
    serializer_class = create_Dispatchserializers
    pagination_class = StandardResultsSetPagination


class Salesman_ListView(viewsets.ModelViewSet):
    queryset = Salesman_List.objects.all()
    serializer_class = Salesman_Listserializers
    pagination_class = StandardResultsSetPagination


class Create_DispatchReqnoView(viewsets.ModelViewSet):
    
    queryset = Create_DispatchModels.objects.all()
    serializer_class = create_Dispatchserializers

    def list(self, request, *args, **kwargs):
        # Extracting SALESMAN_NO from the URL as kwargs (or use request.GET for query parameters)
        SALESMAN_NO = kwargs.get('SALESMAN_NO')
        
        # Check if SALESMAN_NO is provided
        if SALESMAN_NO is None:
            return Response({"error": "SALESMAN_NO is required"}, status=400)
        
        # Filter queryset by the provided SALESMAN_NO
        queryset = self.get_queryset().filter(SALESMAN_NO=SALESMAN_NO)
        
        if queryset.exists():
            # Get the highest REQ_ID from the filtered results
            highest_serial_no = queryset.order_by('-REQ_ID').first().REQ_ID
        else:
            # If no records exist, assume REQ_ID as 0
            highest_serial_no = 0  
        
        # Return the highest REQ_ID
        return Response({"REQ_ID": highest_serial_no})
    

class Filtered_balanceDispatchView(viewsets.ModelViewSet):
    queryset = Create_DispatchModels.objects.all()
    serializer_class = create_Dispatchserializers

    @action(detail=False, methods=['get'])
    def filter_dispatch(self, request):
        # Get the salesman number and invoice number from query parameters
        salesman_no = self.request.query_params.get('SALESMAN_NO', None)
        invoice_number = self.request.query_params.get('INVOICE_NUMBER', None)

        # Ensure both parameters are provided
        if salesman_no and invoice_number:
            # Filter based on the salesman number and invoice number
            queryset = Create_DispatchModels.objects.filter(
                SALESMAN_NO=salesman_no,
                INVOICE_NUMBER=invoice_number
            ).values('INVENTORY_ITEM_ID', 'DISPATCHED_QTY')

            # Check if any results are found and return the filtered data
            if queryset.exists():
                return Response(queryset)
            else:
                return Response({'detail': 'No records found'}, status=404)

        # Return an error if parameters are missing
        return Response({'detail': 'Please provide both SALESMAN_NO and INVOICE_NUMBER in the URL'}, status=400)