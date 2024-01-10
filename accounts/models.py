import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator


class Vendor(AbstractUser):
    first_name = None
    last_name = None
    name = models.CharField(max_length=255)
    email = models.EmailField(
        unique=True,
        max_length=128,
    )
    contact_details = models.TextField( unique = True)
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
