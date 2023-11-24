from rest_framework.views import APIView
from rest_framework.response import Response
import uuid
from dboperators.dboperators import serializer_save, update_record
from ...models import Vendor
from ...serializers import VendorSerializer



class ManageVendor(APIView):
    """
    This API is used to Register , fetch,update,detete New Vendor for the given Creds
    """
    def get(self, request, vendor_id):
        vendor_id = vendor_id
        output_json = fetch_vendor_detail_json(vendor_id)
        return Response(output_json)
  
    def post(self, request):
        input_json = request.data
        json_params = input_json
        output_json = create_vendor_json(json_params)
        return Response(output_json)
    
    def put(self, request,vendor_id):
        input_json = request.data
        json_params = input_json
        output_json = update_vendor_json(json_params, vendor_id)
        return Response(output_json)
    

    def delete(self, request,vendor_id):
        output_json = delete_vendor_json( vendor_id)
        return Response(output_json)



# fetch single vendor details 
def fetch_vendor_detail_json(vendor_id):
    output_json =  []
    try:
        # ######################################################
        # Write API Logic here
        # ######################################################
        vendor_exist = Vendor.objects.filter(vendor_id = vendor_id).exists()
        if not vendor_exist:
            output_json = dict(zip(['Status', 'Message',"Payload"],
                               [404, f"Vendor Not Found", None]))
            return output_json
        output_payload = {}
        vendor_detail = Vendor.objects.filter(vendor_id = vendor_id)
        vendor_detail_serializer = VendorSerializer(vendor_detail, many=True).data
        output_payload = vendor_detail_serializer

        output_json = dict(zip(['Status', 'Message',"Payload"],
                               [200, f"Fetch the vender details successfully", output_payload]))

        # ##############################################################################################
        # Write API logic above
        # ##############################################################################################
        return output_json

    except Exception as ex:
        output_json = dict(zip(['Status', 'Message', 'Request_details', 'Payload'],
                               [404, f"Exception is : {ex}", None, None]))
        return output_json





# create a new vendor 
def create_vendor_json(request):
    input_json, output_json = request, []
    try:
        # ######################################################
        # Write API Logic here
        # ######################################################

        vendor_details = dict(zip(["first_name","last_name","email_id","phone_no","address"],
                                  [input_json['first_name'],input_json['last_name'],input_json['email'],input_json['phone'],input_json['address']]))
        vendor_details = serializer_save(VendorSerializer, vendor_details).data

        output_json = dict(zip(['Status', 'Message',"Payload"],
                               [200, f"vendor has been  Created successfully", vendor_details]))

        # ##############################################################################################
        # Write API logic above
        # ##############################################################################################
        return output_json

    except Exception as ex:
        output_json = dict(zip(['Status', 'Message', 'Request_details', 'Payload'],
                               [404, f"Exception is : {ex}", None, None]))
        return output_json
    




# create a new vendor 
def update_vendor_json(request,vendor_id):
    input_json, output_json = request, []
    try:
        # ######################################################
        # Write API Logic here
        # ######################################################
        vendor_exist = Vendor.objects.filter(vendor_id = vendor_id).exists()
        if not vendor_exist:
            output_json = dict(zip(['Status', 'Message',"Payload"],
                               [404, f"Vendor Not Found", None]))
            return output_json

        vendor_details = update_record(Vendor, vendor_id,
                                    first_name = input_json['first_name'],
                                    last_name = input_json['last_name'],
                                    email_id = input_json['email'],
                                    phone_no = input_json['phone'],
                                    address = input_json['address'],
                                    on_time_delivery_rate = input_json['on_time_delivery_rate'],
                                    quality_rating_avg = input_json['quality_rating_avg'],
                                    average_response_time = input_json['average_response_time'],
                                    fulfillment_rate = input_json['fulfillment_rate']
                                     )

        output_json = dict(zip(['Status', 'Message',"Payload"],
                               [200, f"vendor detail updated successfully", vendor_details]))

        # ##############################################################################################
        # Write API logic above
        # ##############################################################################################
        return output_json

    except Exception as ex:
        output_json = dict(zip(['Status', 'Message', 'Request_details', 'Payload'],
                               [404, f"Exception is : {ex}", None, None]))
        return output_json
    



# create a new vendor 
def delete_vendor_json(vendor_id):
    output_json = []
    try:
        # ######################################################
        # Write API Logic here
        # ######################################################
        vendor_exist = Vendor.objects.filter(vendor_id = vendor_id).exists()
        if not vendor_exist:
            output_json = dict(zip(['Status', 'Message',"Payload"],
                               [404, f"Vendor Not Found", None]))
            return output_json
        
        delete_vendor = Vendor.objects.filter(vendor_id = vendor_id).delete()

        output_json = dict(zip(['Status', 'Message'],
                               [200, f"Vendor deleted successfully"]))

        # ##############################################################################################
        # Write API logic above
        # ##############################################################################################
        return output_json

    except Exception as ex:
        output_json = dict(zip(['Status', 'Message', 'Request_details', 'Payload'],
                               [404, f"Exception is : {ex}", None, None]))
        return output_json
    



