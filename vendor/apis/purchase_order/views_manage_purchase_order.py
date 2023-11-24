from rest_framework.views import APIView
from rest_framework.response import Response
import uuid
from dboperators.dboperators import serializer_save, update_record
from ...models import PurchaseOrder, PurchaseOrderStatus,PerformanceRecord
from ...serializers import PurchaseOrderSerializer,PurchaseOrderStatusSerializer, PerformanceRecordSerializer
from datetime import datetime,timedelta


class ManagePurchaseOrder(APIView):
    """
    This API is used to create, fetch , update ,delete order.
    """
    
    def post(self, request):
        input_json = request.data
        json_params = input_json
        output_json = create_purchase_order_json(json_params)
        return Response(output_json)
    

    def get(self, request, po_id):
        output_json = get_purchase_order_json(po_id)
        return Response(output_json)
    
    def put(self, request,po_id):
        input_json = request.data
        json_params = input_json
        output_json = update_purchase_order_json(json_params, po_id)
        return Response(output_json)
    
    def delete(self, request,po_id):
        output_json = delete_purchase_order_json(po_id)
        return Response(output_json)
    


# Create Purchase order
def create_purchase_order_json(request):
    input_json, output_json = request, []
    try:
        # ######################################################
        # Write API Logic here
        # ######################################################
        output_payload = {}
        today_date = datetime.now()
        delivery_days = input_json['delivery_days']
        delivery_date = (datetime.now() + timedelta(days=delivery_days))
        
        # create purchase order 
        order_details = dict(zip(["vendor","order_date","delivery_date","items","quantity","order_status","quality_rating","issue_date"],
                                  
                                  [input_json['vendor'],today_date,delivery_date,input_json['items'],input_json['quantity'],1,None,today_date]))
        order_details = serializer_save(PurchaseOrderSerializer, order_details).data
        output_payload = order_details

        # create performance details for this vendor
        performance_detail = dict(zip(["vendor","added_date"],
                                      [input_json['vendor'],today_date]))
        performance_detail_create =serializer_save(PerformanceRecordSerializer,performance_detail)


        # get order status name 
        order_status = PurchaseOrderStatus.objects.get(status_id =output_payload["order_status"] ).status_name
        output_payload['order_status_name'] = order_status
        

        output_json = dict(zip(['Status', 'Message',"Payload"],
                               [200, f"Create purchase order successfully", output_payload]))

        # ##############################################################################################
        # Write API logic above
        # ##############################################################################################
        return output_json

    except Exception as ex:
        output_json = dict(zip(['Status', 'Message', 'Request_details', 'Payload'],
                               [404, f"Exception is : {ex}", None, None]))
        return output_json





# get Purchase order details
def get_purchase_order_json(po_id):
    output_json = []
    try:
        # ######################################################
        # Write API Logic here
        # ######################################################
        output_payload = {}

        order_exist = PurchaseOrder.objects.filter(po_number = po_id).exists()
        if not order_exist:
            output_json = dict(zip(['Status', 'Message',"Payload"],
                               [404, f"Order Not Found", None]))
            return output_json


        order_details = PurchaseOrder.objects.filter(po_number=po_id)
        order_details_serializer = PurchaseOrderSerializer(order_details, many=True).data[0]
        output_payload = order_details_serializer
        # get order status name 
        order_status = PurchaseOrderStatus.objects.get(status_id =order_details_serializer["order_status"] ).status_name
        output_payload['order_status_name'] = order_status
        

        output_json = dict(zip(['Status', 'Message',"Payload"],
                               [200, f"get purchase order details successfully", output_payload]))

        # ##############################################################################################
        # Write API logic above
        # ##############################################################################################
        return output_json

    except Exception as ex:
        output_json = dict(zip(['Status', 'Message', 'Request_details', 'Payload'],
                               [404, f"Exception is : {ex}", None, None]))
        return output_json


#update purchase_order
def update_purchase_order_json(request,po_id):
    input_json, output_json = request, []
    try:
        # ######################################################
        # Write API Logic here
        # ######################################################
        order_exist = PurchaseOrder.objects.filter(po_number = po_id).exists()
        if not order_exist:
            output_json = dict(zip(['Status', 'Message',"Payload"],
                               [404, f"Order Not Found", None]))
            return output_json

        order_details = update_record(PurchaseOrder, po_id,
                                    delivery_date = input_json["delivery_date"],
                                    items =input_json["items"],
                                    quantity = input_json["quantity"],
                                    order_status = input_json["order_status"],
                                    quality_rating = input_json["quality_rating"],
                                    issue_date = input_json["issue_date"],
                                    acknowledgment_date = input_json["acknowledgment_date"]
                                     )
        # get order status name 
        order_status = PurchaseOrderStatus.objects.get(status_id =order_details["order_status_id"] ).status_name
        order_details['order_status_name'] = order_status

        output_json = dict(zip(['Status', 'Message',"Payload"],
                               [200, f"order detail updated successfully", order_details]))

        # ##############################################################################################
        # Write API logic above
        # ##############################################################################################
        return output_json

    except Exception as ex:
        output_json = dict(zip(['Status', 'Message', 'Request_details', 'Payload'],
                               [404, f"Exception is : {ex}", None, None]))
        return output_json
    


#delte purchase order
def delete_purchase_order_json(po_id):
    output_json = []
    try:
        # ######################################################
        # Write API Logic here
        # ######################################################
        order_detail = PurchaseOrder.objects.filter(po_number = po_id)
        if not order_detail.exists():
            output_json = dict(zip(['Status', 'Message',"Payload"],
                               [404, f"Order Not Found", None]))
            return output_json
        order_detail.delete()

       
        output_json = dict(zip(['Status', 'Message',"Payload"],
                               [200, f"order detail deleted successfully", None]))

        # ##############################################################################################
        # Write API logic above
        # ##############################################################################################
        return output_json

    except Exception as ex:
        output_json = dict(zip(['Status', 'Message', 'Request_details', 'Payload'],
                               [404, f"Exception is : {ex}", None, None]))
        return output_json
    
