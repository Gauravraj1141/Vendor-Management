from rest_framework.views import APIView
from rest_framework.response import Response
import uuid
from dboperators.dboperators import serializer_save, update_record
from ...models import PurchaseOrder, PurchaseOrderStatus,PerformanceRecord
from ...serializers import PurchaseOrderSerializer,PurchaseOrderStatusSerializer
from datetime import datetime,timedelta


class PoAcknowledge(APIView):
    """
    This API is used acknowledge the vendor
    """
    def post(self, request,po_id):
        input_json = request.data
        json_params = input_json

        output_json = purchase_order_acknowledge_json(json_params,po_id)
        return Response(output_json)


# purchase_order_acknowledge
def purchase_order_acknowledge_json(request,po_id):
    input_json, output_json = request, []
    try:
        # ######################################################
        # Write API Logic here
        # ######################################################
        output_payload = {}
        today_date = datetime.now()
        acknowledge_detail_update = PurchaseOrder.objects.filter(po_number=po_id)

        acknowledge_detail_update.update(acknowledgment_date=today_date)
        vendor_id = acknowledge_detail_update.values()[0]['vendor_id']

        issued_date = acknowledge_detail_update.values()[0]['issue_date']
        acknowledge_date = acknowledge_detail_update.values()[0]['acknowledgment_date']

        issue_date = datetime.fromisoformat(str(issued_date))
        acknowledgment_date = datetime.fromisoformat(str(acknowledge_date))

        # Calculate the time difference
        time_difference = issue_date - acknowledgment_date
        acknowledge_response_time  = time_difference.days
        PerformanceRecord.objects.filter(vendor=vendor_id).update(average_response_time=acknowledge_response_time)

        output_payload = issued_date

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
