from rest_framework import permissions


class IsUserOrSignUp(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        METHODS = permissions.SAFE_METHODS + ('POST',)
        if request.method in METHODS:
            return True
        return obj == request.user
