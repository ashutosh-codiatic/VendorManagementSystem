from rest_framework import serializers
from accounts.models import Vendor
from performance_metrics.models import HistoricalPerformance
from django.utils.translation import gettext as _


class VendorSerializer(serializers.ModelSerializer):
    """Vendor Serializer class 

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model = Vendor
        fields = "__all__"
        read_only_fields = [
            "id",
            "vendor_code",
        ]
        


class VendorPerformanceSerializer(serializers.ModelSerializer):
    """Vendor Serializer class for Performance matrics

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model = Vendor
        fields = [
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]


class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    """History Performance Serializer class for trackig History

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model = HistoricalPerformance
        fields = "__all__"
