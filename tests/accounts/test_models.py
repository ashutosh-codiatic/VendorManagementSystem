from django.test import TestCase, Client

from tests.factory import VendorFactory

class TestAccount(TestCase):
    breakpoint()
    def setUp(self):
        self.vendor = VendorFactory()

    