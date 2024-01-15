from django.dispatch import Signal, receiver
from performance_metrics.models import HistoricalPerformance

performance_history_model = HistoricalPerformance
purchase_order_status_completed = Signal()
purchase_order_acknowledged = Signal()


@receiver(signal=purchase_order_status_completed)
def calculate_perfomance_matrix(sender, instance, **kwargs):
    vendor = instance.vendor
    on_time_delivery_rate = vendor.calculate_on_time_delivery_rate()
    quality_rating_avg = vendor.calculate_avg_quality_ratings()
    fulfillment_rate = vendor.calculate_fulfillment_rate()

    vendor.on_time_delivery_rate = on_time_delivery_rate
    vendor.quality_rating_avg = quality_rating_avg
    vendor.fulfillment_rate = fulfillment_rate
    vendor.save()
    vendor.refresh_from_db()

    performance_history_model.objects.create(
        vendor=vendor,
        on_time_delivery_rate=on_time_delivery_rate,
        quality_rating_avg=quality_rating_avg,
        fulfillment_rate=fulfillment_rate,
        average_response_time=vendor.average_response_time,
    )
    return vendor


@receiver(signal=purchase_order_acknowledged)
def calculate_avg_response_time(sender, instance, **kwargs):
    vendor = instance.vendor
    vendor.avg_response_time = vendor.calculate_avg_response_time()
    vendor.save()

    return vendor
