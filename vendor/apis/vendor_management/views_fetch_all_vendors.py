from rest_framework.views import APIView
from rest_framework.response import Response
import uuid
from dboperators.dboperators import serializer_save
from ...models import Vendor
from ...serializers import VendorSerializer


class FetchAllVendors(APIView):
    """
    This API is used to fetch all Vendors
    """
    def get(self, request):
        output_json = fetch_all_vendors_json()
        return Response(output_json)


# fetch all vendors details 
def fetch_all_vendors_json():
    output_json =  []
    try:
        # ######################################################
        # Write API Logic here
        # ######################################################
        output_payload = {}
        vendor_details = Vendor.objects.all()
        vendor_details_serializer = VendorSerializer(vendor_details, many=True).data
        output_payload = vendor_details_serializer

        output_json = dict(zip(['Status', 'Message',"Payload"],
                               [200, f"Fetch all the venders details successfully", output_payload]))

        # ##############################################################################################
        # Write API logic above
        # ##############################################################################################
        return output_json

    except Exception as ex:
        output_json = dict(zip(['Status', 'Message', 'Request_details', 'Payload'],
                               [404, f"Exception is : {ex}", None, None]))
        return output_json
