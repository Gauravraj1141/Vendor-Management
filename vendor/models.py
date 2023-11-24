from django.db import models
import uuid
from datetime import datetime

class Vendor(models.Model):
    def generate_unique_code():
        return str(uuid.uuid4().hex)[:6]
    
    vendor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, default=None)
    last_name = models.CharField(max_length=100, default=None)
    email_id = models.EmailField(max_length=100,default=None, unique=True)
    phone_no = models.IntegerField(null=True,blank=True)
    vendor_code = models.CharField(max_length=6, default=generate_unique_code, unique=True)
    address = models.TextField(null=True,blank=True)
    on_time_delivery_rate = models.FloatField(null=True,blank=True)
    quality_rating_avg = models.FloatField(null=True,blank=True)
    average_response_time = models.FloatField(null=True,blank=True)
    fulfillment_rate = models.FloatField(null=True,blank=True)

   
    def __str__(self):
        return str(self.vendor_id)
    

class PurchaseOrderStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.status_id)
    

class PurchaseOrder(models.Model):
    po_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,related_name="purchase_vendor")
    order_date =  models.DateTimeField(default=datetime.now)
    delivery_date = models.DateTimeField(default=datetime.now)
    items = models.JSONField()
    quantity = models.IntegerField()
    order_status = models.ForeignKey(PurchaseOrderStatus, on_delete=models.CASCADE, related_name='purchase_order_status')
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(default=datetime.now)
    acknowledgment_date = models.DateTimeField(default=datetime.now, null=True, blank=True)

    def __str__(self):
        return str(self.po_number)
    

class PerformanceRecord(models.Model):
    performance_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,related_name="vendor_performance")
    added_date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField(null=True,blank=True)
    quality_rating_avg = models.FloatField(null=True,blank=True)
    average_response_time = models.FloatField(null=True,blank=True)
    fulfillment_rate = models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.performance_id)