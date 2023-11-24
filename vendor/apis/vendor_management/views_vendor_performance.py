from rest_framework.views import APIView
from rest_framework.response import Response
import uuid
from dboperators.dboperators import serializer_save
from ...models import Vendor,PurchaseOrder, PerformanceRecord
from ...serializers import VendorSerializer, PurchaseOrderSerializer, PerformanceRecordSerializer


class VendorPerformance(APIView):
    """
    This API is used to calculate the performance of vendor
    """
    def get(self, request,vendor_id):
        output_json = calculate_vendor_performance_json(vendor_id)
        return Response(output_json)


# fetch all vendors details 
def calculate_vendor_performance_json(vendor_id):
    output_json =  []
    try:
        # ######################################################
        # Write API Logic here
        # ######################################################
        vendor_exist = PerformanceRecord.objects.filter(vendor = vendor_id).exists()
        if not vendor_exist:
            output_json = dict(zip(['Status', 'Message',"Payload"],
                               [404, f"Vendor performance Not Found", None]))
            return output_json
        
        output_payload = {}
        performance_details = PerformanceRecord.objects.filter(vendor=vendor_id)
        performance_details_serializer = PerformanceRecordSerializer(performance_details, many=True).data
        output_payload = performance_details_serializer

        output_json = dict(zip(['Status', 'Message',"Payload"],
                               [200, f"Fetch the vendor performance successfully", output_payload]))

        # ##############################################################################################
        # Write API logic above
        # ##############################################################################################
        return output_json

    except Exception as ex:
        output_json = dict(zip(['Status', 'Message', 'Request_details', 'Payload'],
                               [404, f"Exception is : {ex}", None, None]))
        return output_json
