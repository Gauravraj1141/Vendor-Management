from django.urls import path
from vendor.apis.vendor_management.views_manage_vendor import ManageVendor
from vendor.apis.vendor_management.views_fetch_all_vendors import FetchAllVendors
from vendor.apis.purchase_order.views_manage_purchase_order import ManagePurchaseOrder
from vendor.apis.purchase_order.views_get_all_purchase_order import GetAllPurchaseOrder

urlpatterns = [
    path("vendors/all/",FetchAllVendors.as_view()),
    path("vendors/",ManageVendor.as_view()),
    path("vendors/<uuid:vendor_id>/", ManageVendor.as_view(), name="vendor-detail"),
    path("vendors/<uuid:vendor_id>/", ManageVendor.as_view(), name="vendor-detail"),

    path("purchase_orders/", ManagePurchaseOrder.as_view(), name="purchase-order"),
    path("purchase_orders/<uuid:po_id>/", ManagePurchaseOrder.as_view(), name="purchase-order-detail"),
    path("purchase_orders/all", GetAllPurchaseOrder.as_view(), name="all-order"),
    path("purchase_orders/all", GetAllPurchaseOrder.as_view(), name="all-order"),


]
