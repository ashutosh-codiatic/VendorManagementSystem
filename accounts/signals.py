# from django.conf import settings
import uuid
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from accounts.models import Vendor

# @receiver(post_save, sender=Vendor)
# def create_freelancer(sender, instance, created, **kwargs):
#     if created:
#         instance.vendor_code = f"{instance.id}_{uuid.uuid4()}"
#         instance.save()


@receiver(pre_save, sender=Vendor)
def create_freelancer(sender, instance, **kwargs):
    if not instance.vendor_code:
        instance.vendor_code = f"{uuid.uuid4()}"
        return 
