from django.core.exceptions import PermissionDenied
from rest_framework import permissions

class CorrectOrganizationMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if self.organization != request.user.organization:
            raise PermissionDenied
        else:
            return super(CorrectOrganizationMixin, self).dispatch(request, *args, **kwargs)