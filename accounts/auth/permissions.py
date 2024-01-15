from rest_framework import permissions
from rest_framework.permissions import BasePermission


class CustomVendorPermission(BasePermission):
    """Custom Permission for Vendor

    Args:
        BasePermission (class):A base class from which all permission
        classes should inherit.
    """

    def has_object_permission(self, request, view, obj):
        if obj.id == request.user.id:
            return True
        else:
            return request.method in permissions.SAFE_METHODS
