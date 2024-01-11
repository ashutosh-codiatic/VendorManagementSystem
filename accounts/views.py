# vendors/views.py
from rest_framework import generics
from rest_framework.response import Response
from accounts.models import Vendor
from accounts.serializers import (
    VendorSerializer,
    VendorPerformanceSerializer,
    HistoricalPerformanceSerializer,
)
from performance_metrics.models import HistoricalPerformance
from rest_framework.permissions import IsAuthenticated


#############################################
# create ModelViewSet with action decorator #
#############################################


# class VendorPerformanceView(generics.RetrieveAPIView):
#     queryset = Vendor.objects.all()
#     serializer_class = VendorSerializer

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()

#         latest_performance = (
#             HistoricalPerformance.objects.filter(vendor=instance)
#             .order_by("-date")
#             .first()
#         )

#         if latest_performance:
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


# class VendorListView(generics.ListCreateAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = Vendor.objects.all()
#     serializer_class = VendorSerializer


# class VendorActionView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = Vendor.objects.all()
#     serializer_class = VendorSerializer


class VendorPerformanceView(generics.RetrieveAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Vendor.objects.all()
    serializer_class = VendorPerformanceSerializer


class VendorPerformanceHistoryView(generics.ListAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
