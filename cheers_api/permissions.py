from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Returns boolean if the user is the owner or not
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
