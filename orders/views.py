from datetime import timezone

from rest_framework import filters, generics, viewsets
from rest_framework.response import Response

from orders.models import PurchaseOrder
from orders.serializers import (
    PurchaseOrderSerializer,
    PurchaseOrderAcknowledgeSerializer,
)
from performance_metrics.models import HistoricalPerformance
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["vendor__name"]


class PurchaseOrderAcknowledgeView(generics.UpdateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderAcknowledgeSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid()
        self.perform_update(serializer=serializer)
        return Response(
            {
                "status": "success",
                "message": "Purchase order has been successfully acknowledged.",
                "code": "success_acknowledgement",
            },
            status=status.HTTP_200_OK,
        )
