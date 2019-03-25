from rest_framework import permissions
from django.contrib.auth import get_user_model
from django.http import Http404


User = get_user_model()


class IsOwnerOrIsStaffPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            user = User.objects.get(pk=view.kwargs['pk'])
        except User.DoesNotExist:
            raise Http404
        if request.user == user:
            return True
        elif request.user.is_staff:
            return True
        return False


class IsStaffOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False
