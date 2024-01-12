# from django.conf import settings
import uuid
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from accounts.models import Vendor
from orders.models import PurchaseOrder
from django.db.models import Count, Avg, F


@receiver(pre_save, sender=Vendor)
def create_freelancer(sender, instance, **kwargs):
    if not instance.vendor_code:
        instance.vendor_code = f"{uuid.uuid4()}"
        return

