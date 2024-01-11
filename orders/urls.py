from django.urls import include, path
from rest_framework.routers import DefaultRouter
from orders import views


from orders.views import  PurchaseOrderViewSet

app_name = "orders"

router = DefaultRouter()
router.register(r"purchase_orders", PurchaseOrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path(
    #     "purchase_orders/<int:pk>/acknowledge/",
    #     AcknowledgePurchaseOrderView.as_view(),
    #     name="acknowledge-purchase-order",
    # ),
    # path("", views.PurchaseOrderListView.as_view(), name="purchase-order-list"),
    # path(
    #     "purchase_order/<int:pk>/",
    #     views.PurchaseOrderActionView.as_view(),
    #     name="purchase-order-actions",
    # ),
    path(
        "purchase_orders/<int:pk>/acknowledge/",
        views.PurchaseOrderAcknowledgeView.as_view(),
        name="purchase-order-acknowledge",
    ),
]
