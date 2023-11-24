from rest_framework import serializers
from . models import *


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'


class PurchaseOrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderStatus
        fields = '__all__'


class PerformanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceRecord
        fields = '__all__'