from common.choices import UserRole, UserStatus
from rest_framework.permissions import BasePermission
from common import validators


class OnlyOwnerPermission(BasePermission):
    message = validators.NO_SERVICE_PERMISSION_MESSAGE
    def has_permission(self, request, view):
        if (request.user.role == UserRole.OWNER or request.user.role == UserRole.MANAGER) and request.user.status == UserStatus.REGISTERED:
            return True
        return False


class OwnerOrManagerPermission(BasePermission):
    message = validators.NO_SERVICE_PERMISSION_MESSAGE
    def has_permission(self, request, view):
        if request.user.role != UserRole.STAFF or request.user.status == UserStatus.REGISTERED:
            return True
        return False


