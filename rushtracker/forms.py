from django.forms import ModelForm, DateInput, PasswordInput, widgets
from rushtracker.models import Rush
from crispy_forms.helper import FormHelper
from authentication.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit, Hidden, Div
from django import forms
from django.db import models
from django.core.urlresolvers import reverse
from base64 import b64decode
from django.core.files.base import ContentFile
from django.contrib.auth import get_user_model
import uuid


class UpdateForm(ModelForm):
    pic64Value = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Rush
        exclude = ['organization', 'picture']
        widgets = {
            'contacted_date': DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.fields[
            'primary_contact'].queryset = get_user_model().tenant_objects.all()
        self.fields[
            'secondary_contact'].queryset = get_user_model().tenant_objects.all()
        self.fields['rush_period'].queryset = self.request.user.organization.rushperiod_set.all()
        self.helper = FormHelper(self)
        self.helper['rush_period'].wrap(Field, css_class="chosen-select")
        self.helper.add_input(
            Submit('submit', 'Update', css_class='btn-primary'))

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError(
                "Can't create User and UserProfile without database save")
        rush = super(UpdateForm, self).save(commit=False)
        if self.cleaned_data['pic64Value'] != '':
            image_data = b64decode(self.cleaned_data['pic64Value'][22:])
            image_name = str(uuid.uuid1())
            rush.picture = ContentFile(image_data, image_name)
        self.save_m2m()
        rush.save()
        print rush.picture


class CreateRushForm(forms.ModelForm):
    pic64Value = forms.CharField(required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CreateRushForm, self).__init__(*args, **kwargs)
        self.fields[
            'primary_contact'].queryset = get_user_model().tenant_objects.all()
        self.fields[
            'secondary_contact'].queryset = get_user_model().tenant_objects.all()
        self.fields['rush_period'].queryset = self.request.user.organization.rushperiod_set.all()
        if self.request.user.organization.active_rush_period:
            self.fields['rush_period'].initial = ([self.request.user.organization.active_rush_period, ])
        self.helper = FormHelper(self)
        self.helper['contacted_date'].wrap(Field, css_class="datepicker")
        self.helper['rush_period'].wrap(Field, css_class="chosen-select")
        self.helper.add_input(
            Submit('submit', 'Submit', css_class='btn-primary'))

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError(
                "Can't create User and UserProfile without database save")
        rush = super(CreateRushForm, self).save(commit=False)
        rush.organization = self.request.user.organization
        if self.cleaned_data['pic64Value'] != '':
            image_data = b64decode(self.request.POST['pic64Value'][22:])
            image_name = str(uuid.uuid1())
            rush.picture = ContentFile(image_data, image_name)
            print("here");
        
        else: 
            rush.picture = 'profile_picture/default_picture.png'
            print ('Heres')
        rush.save()
        self.save_m2m()

    class Meta:
        model = Rush
        exclude = ['organization', 'picture']
