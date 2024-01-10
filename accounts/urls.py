from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.auth.views import VendorRegistrationViewSet, VendorLoginViewSet

# router = DefaultRouter()
# router.register(r"vendors", RegistrationViewSet, basename="vendor")


# urlpatterns = []

# urlpatterns += router.urls


router = DefaultRouter()
router.register(r"vendors", VendorRegistrationViewSet, basename="vendor")
router.register(r"login", VendorLoginViewSet, basename="vendor")


urlpatterns = [
    path("", include(router.urls)),
    # path(
    #     "api/vendors/<int:pk>/performance/",
    #     VendorPerformanceView.as_view(),
    #     name="vendor-performance",
    # ),
]
