from django.core.management.base import BaseCommand
from orders.models import PurchaseOrder
from performance_metrics.models import HistoricalPerformance
from django.utils import timezone


class Command(BaseCommand):
    help = "Calculate performance metrics and update vendor records"

    def handle(self, *args, **options):
        completed_pos = PurchaseOrder.objects.filter(status="completed")
        for vendor in set(po.vendor for po in completed_pos):
            on_time_delivery_rate = vendor.calculate_on_time_delivery_rate()
            quality_rating_avg = vendor.calculate_avg_quality_ratings()
            fulfillment_rate = vendor.calculate_fulfillment_rate()
            avg_response_time = vendor.calculate_avg_response_time()

            vendor.on_time_delivery_rate = on_time_delivery_rate
            vendor.quality_rating_avg = quality_rating_avg
            vendor.fulfillment_rate = fulfillment_rate
            vendor.average_response_time = avg_response_time
            vendor.save()

            HistoricalPerformance.objects.create(
                vendor=vendor,
                on_time_delivery_rate=on_time_delivery_rate,
                quality_rating_avg=quality_rating_avg,
                fulfillment_rate=fulfillment_rate,
                average_response_time=vendor.average_response_time,
            )

        self.stdout.write(
            self.style.SUCCESS("Metrics calculated and vendors updated successfully.")
        )

