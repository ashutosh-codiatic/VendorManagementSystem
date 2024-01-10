# from django.db import models
# from vendors.models import Vendor  # Assuming you have a Vendor model


# class HistoricalPerformance(models.Model):
#     vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
#     date = models.DateTimeField()
#     on_time_delivery_rate = models.FloatField()
#     quality_rating_avg = models.FloatField()
#     average_response_time = models.FloatField()
#     fulfillment_rate = models.FloatField()

#     def calculate_on_time_delivery_rate(self):
#         completed_orders = PurchaseOrder.objects.filter(
#             vendor=self.vendor,
#             status="completed",
#             delivery_date__lte=models.F("acknowledgment_date"),
#         )
#         total_orders = PurchaseOrder.objects.filter(
#             vendor=self.vendor, status="completed"
#         )

#         on_time_delivery_rate = (
#             (completed_orders.count() / total_orders.count()) * 100
#             if total_orders.count() > 0
#             else 0
#         )
#         return on_time_delivery_rate

#     def calculate_quality_rating_avg(self):
#         completed_orders = PurchaseOrder.objects.filter(
#             vendor=self.vendor, status="completed", quality_rating__isnull=False
#         )
#         quality_rating_avg = completed_orders.aggregate(models.Avg("quality_rating"))[
#             "quality_rating__avg"
#         ]
#         return quality_rating_avg
    

#     def calculate_average_response_time(self):
#         completed_orders = PurchaseOrder.objects.filter(vendor=self.vendor, status='completed', acknowledgment_date__isnull=False)
#         response_times = (order.acknowledgment_date - order.issue_date).total_seconds() / 60 for order in completed_orders)
#         average_response_time = sum(response_times) / len(response_times) if len(response_times) > 0 else 0
#         return average_response_time

#     def calculate_fulfillment_rate(self):
#         fulfilled_orders = PurchaseOrder.objects.filter(vendor=self.vendor, status='completed')
#         total_orders = PurchaseOrder.objects.filter(vendor=self.vendor)
#         fulfillment_rate = (fulfilled_orders.count() / total_orders.count()) * 100 if total_orders.count() > 0 else 0
#         return fulfillment_rate