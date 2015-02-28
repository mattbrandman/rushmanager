from django.forms import ModelForm, DateInput, PasswordInput
from rushtracker.models import Rush
from crispy_forms.helper import FormHelper
from authentication.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit, Hidden
from django import forms
from django.core.urlresolvers import reverse


class DetailForm(ModelForm):

    class Meta:
        model = Rush
        widgets = {
            'contacted_date': DateInput(attrs={'type': 'date'})}
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Update', css_class='btn-primary'))

class CreateRushForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateRushForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper['contacted_date'].wrap(Field, css_class="datepicker")
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

    class Meta:
        model = Rush

