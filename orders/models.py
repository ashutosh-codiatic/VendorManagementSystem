from django.db import models
from accounts.models import Vendor

PENDING = "pending"
COMPLETED = "completed"
CANCELED = "canceled"
order_status = [(PENDING, "pending"), (COMPLETED, "completed"), (CANCELED, "canceled")]


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=10)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=9, choices = order_status)
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField()

    