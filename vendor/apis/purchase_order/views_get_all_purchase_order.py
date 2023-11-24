from rest_framework.views import APIView
from rest_framework.response import Response
import uuid
from dboperators.dboperators import serializer_save, update_record
from ...models import PurchaseOrder, PurchaseOrderStatus
from ...serializers import PurchaseOrderSerializer,PurchaseOrderStatusSerializer
from datetime import datetime,timedelta


class GetAllPurchaseOrder(APIView):
    """
    This API is used to fetch all Orders
    """
    def get(self, request):

        output_json = get_all_purchase_order()
        return Response(output_json)


# fetch all orders details 
def get_all_purchase_order():
    output_json =  []
    try:
        # ######################################################
        # Write API Logic here
        # ######################################################
        output_payload = {}
        order_details = PurchaseOrder.objects.all()
        order_details_serializer = PurchaseOrderSerializer(order_details, many=True).data

        purchase_order_list = []
        for order_details in order_details_serializer:
            
            order_status = PurchaseOrderStatus.objects.get(status_id =order_details["order_status"] ).status_name
            order_details['order_status_name'] = order_status
            purchase_order_list.append(order_details)


        output_payload = purchase_order_list

        output_json = dict(zip(['Status', 'Message',"Payload"],
                               [200, f"Fetch all the orders details successfully", output_payload]))

        # ##############################################################################################
        # Write API logic above
        # ##############################################################################################
        return output_json

    except Exception as ex:
        output_json = dict(zip(['Status', 'Message', 'Request_details', 'Payload'],
                               [404, f"Exception is : {ex}", None, None]))
        return output_json
