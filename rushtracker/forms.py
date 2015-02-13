from django.forms import ModelForm, DateInput, PasswordInput
from rushtracker.models import Rush, UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from rushtracker.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit
from django import forms


class DetailForm(ModelForm):

    class Meta:
        model = Rush
        widgets = {
            'rush_contacted_date': DateInput(attrs={'type': 'date'})}
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))


class CreateRushForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateRushForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper['rush_contacted_date'].wrap(Field, css_class="datepicker")
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

    class Meta:
        model = Rush
