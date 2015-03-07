import six

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.http import HttpResponseRedirect
from django.utils.encoding import force_text
from braces import AccessMixin

class UserPassesTestMixin(AccessMixin):
    """
    CBV Mixin allows you to define test that every user should pass
    to get access into view.
    Class Settings
        `test_func` - This is required to be a method that takes user
            instance and return True or False after checking conditions.
        `login_url` - the login url of site
        `redirect_field_name` - defaults to "next"
        `raise_exception` - defaults to False - raise 403 if set to True
    """



    def dispatch(self, request, *args, **kwargs):
        user_test_result = request.user.organization == 

        if not user_test_result:  # If user don't pass the test
                return redirect_to_login(request.get_full_path(),
                                         self.get_login_url(),
                                         self.get_redirect_field_name())
        return super(UserPassesTestMixin, self).dispatch(
            request, *args, **kwargs)