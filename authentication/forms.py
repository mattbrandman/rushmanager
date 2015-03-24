from django.forms import ModelForm, DateInput, PasswordInput
from rushtracker.models import Rush
from organization.models import Organization
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from authentication.models import UserProfile
from django.contrib.auth.models import User, Permission
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit, Hidden
from django import forms
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.forms.util import ErrorList
from organization.forms import CreateOrganizationForm
import pdb

class UserSignInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserSignInForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.render_hidden_fields = True
        self.helper.form_tag = False
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn_primary'))

class ChapterAdminForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    fraternity = forms.CharField(max_length=100, required=True)
    chapter = forms.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 
            'email', 'password1', 'password2')
    helper = FormHelper()
    helper.add_input(Submit('Submit', 'Submit', css_class='btn-primary'))
    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(ChapterAdminForm, self).save(commit=True)
        user.user_permissions.add(Permission.objects.get(codename='chapter_admin'),)
        data = {
            'owner' : user.id,
            'national_organization' : self.cleaned_data['fraternity'], 
            'chapter_name' : self.cleaned_data['chapter']
        }
        organization = CreateOrganizationForm(data)
        my_org = organization.save()
        user_profile = UserProfile(user=user, organization=my_org)
        user_profile.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('',)
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    
class SingleUserCreationForm(UserCreationForm):
    helper = FormHelper()
    helper.form_action = '/authentication/createSingleUser'
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('first_name', 'last_name', 'username', 
            'email', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SingleUserCreationForm, self).__init__(*args, **kwargs)
    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(SingleUserCreationForm, self).save(commit=True)
        organization = self.request.user.profile.organization
        user_profile = UserProfile(user=user, organization=organization)
        user_profile.save()
        return user







