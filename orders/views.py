# from rest_framework import viewsets
# from .models import PurchaseOrder
# from .serializers import PurchaseOrderSerializer
# from rest_framework import filters


# class PurchaseOrderViewSet(viewsets.ModelViewSet):
#     queryset = PurchaseOrder.objects.all()
#     serializer_class = PurchaseOrderSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ["vendor__name"]  # Assuming 'name' is a field in your Vendor model


# # purchase_orders/views.py
# from rest_framework import generics
# from rest_framework.response import Response
# from .models import PurchaseOrder, HistoricalPerformance
# from .serializers import PurchaseOrderSerializer


# class AcknowledgePurchaseOrderView(generics.UpdateAPIView):
#     queryset = PurchaseOrder.objects.all()
#     serializer_class = PurchaseOrderSerializer
#     lookup_field = "po_id"

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()

#         # Update acknowledgment_date
#         instance.acknowledgment_date = timezone.now()
#         instance.save()

#         # Trigger recalculation of average_response_time in HistoricalPerformance
#         vendor = instance.vendor
#         historical_performance = (
#             HistoricalPerformance.objects.filter(vendor=vendor)
#             .order_by("-date")
#             .first()
#         )

#         if historical_performance:
#             historical_performance.calculate_average_response_time()
#             historical_performance.save()

#         return Response({"acknowledgment_date": instance.acknowledgment_date})
