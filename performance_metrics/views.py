# # vendors/views.py
# from rest_framework import generics
# from rest_framework.response import Response
# from .models import Vendor
# from purchase_orders.models import PurchaseOrder
# from .serializers import VendorSerializer


# class VendorPerformanceView(generics.RetrieveAPIView):
#     queryset = Vendor.objects.all()
#     serializer_class = VendorSerializer

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()

#         # Calculate performance metrics
#         on_time_delivery_rate = self.calculate_on_time_delivery_rate(instance)
#         quality_rating_avg = self.calculate_quality_rating_avg(instance)
#         average_response_time = self.calculate_average_response_time(instance)
#         fulfillment_rate = self.calculate_fulfillment_rate(instance)

#         # Return the performance metrics along with the vendor details
#         data = {
#             "vendor": VendorSerializer(instance).data,
#             "performance_metrics": {
#                 "on_time_delivery_rate": on_time_delivery_rate,
#                 "quality_rating_avg": quality_rating_avg,
#                 "average_response_time": average_response_time,
#                 "fulfillment_rate": fulfillment_rate,
#             },
#         }

#         return Response(data)

#     def calculate_on_time_delivery_rate(self, vendor):
#         # Implement your logic to calculate on-time delivery rate
#         # Example logic: Count delivered orders by the promised date and calculate the percentage
#         delivered_orders = PurchaseOrder.objects.filter(
#             vendor=vendor,
#             status="completed",
#             delivery_date__lte=models.F("acknowledgment_date"),
#         )
#         total_orders = PurchaseOrder.objects.filter(vendor=vendor, status="completed")
#         on_time_delivery_rate = (
#             (delivered_orders.count() / total_orders.count()) * 100
#             if total_orders.count() > 0
#             else 0
#         )
#         return on_time_delivery_rate

#     def calculate_quality_rating_avg(self, vendor):
#         # Implement your logic to calculate the average quality rating
#         # Example logic: Calculate the average quality rating from the related HistoricalPerformance records
#         historical_performances = HistoricalPerformance.objects.filter(vendor=vendor)
#         quality_rating_avg = historical_performances.aggregate(
#             models.Avg("quality_rating_avg")
#         )["quality_rating_avg__avg"]
#         return quality_rating_avg

#     def calculate_average_response_time(self, vendor):
#         # Implement your logic to calculate the average response time
#         # Example logic: Calculate the average response time from the related HistoricalPerformance records
#         historical_performances = HistoricalPerformance.objects.filter(vendor=vendor)
#         average_response_time = historical_performances.aggregate(
#             models.Avg("average_response_time")
#         )["average_response_time__avg"]
#         return average_response_time

#     def calculate_fulfillment_rate(self, vendor):
#         # Implement your logic to calculate fulfillment rate
#         # Example logic: Count fulfilled purchase orders and calculate the percentage
#         fulfilled_orders = PurchaseOrder.objects.filter(
#             vendor=vendor, status="completed"
#         )
#         total_orders = PurchaseOrder.objects.filter(vendor=vendor)
#         fulfillment_rate = (
#             (fulfilled_orders.count() / total_orders.count()) * 100
#             if total_orders.count() > 0
#             else 0
#         )
#         return fulfillment_rate
