# # vendors/views.py
# from rest_framework import generics
# from rest_framework.response import Response
# from .models import Vendor
# from purchase_orders.models import HistoricalPerformance
# from .serializers import VendorSerializer


# class VendorPerformanceView(generics.RetrieveAPIView):
#     queryset = Vendor.objects.all()
#     serializer_class = VendorSerializer

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()

#         # Retrieve latest HistoricalPerformance record for the vendor
#         latest_performance = (
#             HistoricalPerformance.objects.filter(vendor=instance)
#             .order_by("-date")
#             .first()
#         )

#         if latest_performance:
#             # Return the performance metrics along with the vendor details
#             data = {
#                 "vendor": VendorSerializer(instance).data,
#                 "performance_metrics": {
#                     "on_time_delivery_rate": latest_performance.calculate_on_time_delivery_rate(),
#                     "quality_rating_avg": latest_performance.calculate_quality_rating_avg(),
#                     "average_response_time": latest_performance.calculate_average_response_time(),
#                     "fulfillment_rate": latest_performance.calculate_fulfillment_rate(),
#                 },
#             }
#             return Response(data)
#         else:
#             return Response(
#                 {"error": "No historical performance data available for this vendor."},
#                 status=404,
#             )
