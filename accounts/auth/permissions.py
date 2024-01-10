from rest_framework.permissions import BasePermission


class CustomVendorPermission(BasePermission):
    def has_permission(self, request, view):

        if request.method == "POST":
            return True
        
        if request.user.is_active == True:
            return True

