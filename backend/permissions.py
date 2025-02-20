from rest_framework import permissions

class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='MANAGER'):
            return True
        return False

class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='EMPLOYEE'):
            return True
        return False