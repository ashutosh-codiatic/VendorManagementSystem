from rest_framework import serializers
from orders.models import PurchaseOrder
from django.utils.translation import gettext as _
from orders import signals
from datetime import timezone

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = "__all__"
        

    def validate(self, attrs):
        return super().validate(attrs)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if instance.status == "completed":
            signals.purchase_order_status_completed.send(
                sender=instance.__class__, instance=instance
            )
        return instance


class PurchaseOrderAcknowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ["acknowledgment_date"]
        extra_kwargs = {"acknowledgment_date": {"required": True}}

    def validate_acknowledgment_date(self, value):
        if not value:
            value = timezone.now()
        return value

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        signals.purchase_order_acknowledged.send(
            sender=instance.__class__, instance=instance
        )
        return instance
