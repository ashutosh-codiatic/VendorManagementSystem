import factory
from accounts.models import Vendor


class VendorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vendor
    name = factory.Faker("name")
    email = factory.Faker("email")
    contact_details = factory.Faker("phone_number")
    address = factory.Faker("address")
    vendor_code = factory.Sequence(lambda n: n*n)


