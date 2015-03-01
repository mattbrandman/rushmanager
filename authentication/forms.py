from django.forms import ModelForm, DateInput, PasswordInput
from rushtracker.models import Rush
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from authentication.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit, Hidden
from django import forms
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.forms.util import ErrorList

class AuthenticationFormAny(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthenticationFormAny, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.render_hidden_fields = True
        self.helper.form_tag = False
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn_primary'))

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    organization_token = forms.CharField(max_length=200, required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 
            'email', 'password1', 'password2', 'organization_token')
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

    def is_valid(self):
        valid = super(UserForm, self).is_valid()
        if not valid:
            return valid
        if int(self.cleaned_data['organization_token']) == 1:
            self._errors["organization_token"]  = ErrorList([u"There is no matching token here"])
            return False
    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(UserForm, self).save(commit=True)
       # user_profile = UserProfile(user=user, organization=self.cleaned_data['organization_to'] )
        # user_profile.save()
        return user, #user_profile
        
class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
