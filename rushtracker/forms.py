from django.forms import ModelForm, DateInput, PasswordInput, widgets
from rushtracker.models import Rush
from crispy_forms.helper import FormHelper
from authentication.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit, Hidden
from django import forms
from django.db import models
from django.core.urlresolvers import reverse
from base64 import b64decode
from django.core.files.base import ContentFile, File
import uuid


class DetailForm(ModelForm):

    class Meta:
        model = Rush
        exclude = ['organization',]
        widgets = {
            'contacted_date': DateInput(attrs={'type': 'date'})}
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Update', css_class='btn-primary'))

class CreateRushForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CreateRushForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper['contacted_date'].wrap(Field, css_class="datepicker")
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        
    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        rush = super(CreateRushForm, self).save(commit=False)
        rush.organization = self.request.user.profile.organization
        image_data = self.request.FILES['file']
        print image_data.size
        image_name = str(uuid.uuid1())
        rush.picture = File(file=image_data, name=image_name)
        rush.save()


    class Meta:
        model = Rush
        exclude = ['organization', 'photo']



