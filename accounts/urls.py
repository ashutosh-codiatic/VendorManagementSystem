from django.urls import include, path
from rest_framework.routers import DefaultRouter
from accounts.auth.views import VendorLoginViewSet, VendorRegistrationViewSet
from accounts import views

# router = DefaultRouter()
# router.register(r"vendors", RegistrationViewSet, basename="vendor")


# urlpatterns = []

# urlpatterns += router.urls
app_name = "accounts"


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
    # path("vendors/", views.VendorListView.as_view(), name="vendors-list"),
    # path("vendors/<uuid:pk>/", views.VendorActionView.as_view(), name="vendor-actions"),
    path(
        "vendors/<int:pk>/performance/",
        views.VendorPerformanceView.as_view(),
        name="vendor-performance",
    ),
    path(
        "vendors/<int:pk>/performance/history/",
        views.VendorPerformanceHistoryView.as_view(),
        name="vendor-performance-history",
    ),
]




