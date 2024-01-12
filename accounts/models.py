from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class Vendor(AbstractUser):
    first_name = None
    last_name = None
    name = models.CharField(max_length=255)
    email = models.EmailField(
        unique=True,
        max_length=128,
    )
    contact_details = models.TextField(unique=True)
    address = models.TextField()
    vendor_code = models.CharField(max_length=10, unique=True)
    on_time_delivery_rate = models.FloatField(
        default=0.0, validators=[MinValueValidator(0.0)]
    )
    quality_rating_avg = models.FloatField(
        default=0.0, validators=[MinValueValidator(0.0)]
    )
    average_response_time = models.FloatField(
        default=0.0, validators=[MinValueValidator(0.0)]
    )
    fulfillment_rate = models.FloatField(
        default=0.0, validators=[MinValueValidator(0.0)]
    )

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ("username",)

    def __str__(self) -> str:
        """
        Return a string representation of the user.

        Returns:
        - str: The username of the user.
        """
        return self.email

    def calc_on_time_delivery_rate(self):
        po_list = self.purchaseorder_set.filter(status="completed")
        filter_on_time_deliverables = po_list.filter(
            acknowledgment_date__lte=models.F("delivery_date")
        )
        try:
            return round(filter_on_time_deliverables.count() / po_list.count(), 2)
        except ZeroDivisionError:
            return 0

    def calc_avg_quality_ratings(self):
        po_list = self.purchaseorder_set.filter(status="completed")
        result = po_list.aggregate(
            avg_quality_rating=models.Avg("quality_rating", default=0.0)
        )

        return round(result.get("avg_quality_rating"))

    def calc_fulfillment_rate(self):
        po_list_status_completed = self.purchaseorder_set.filter(status="completed")

        po_list = self.purchaseorder_set.filter(status="pending")

        try:
            return round(po_list_status_completed.count() / po_list.count(), 2)
        except ZeroDivisionError:
            return 0

    def calc_avg_response_time(self):
        filter_po_data = self.purchaseorder_set.filter(
            issue_date__isnull=False, acknowledgment_date__isnull=False
        )

        if filter_po_data.exists():
            result = filter_po_data.aggregate(
                avg_response_time=models.Avg(
                    models.F("acknowledgment_date") - models.F("issue_date")
                )
            )
        try:
            return round(result.get("avg_response_time").total_seconds(), 2)
        except ZeroDivisionError:
            return 0
