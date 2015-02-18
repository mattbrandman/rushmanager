from django.forms import ModelForm, DateInput, PasswordInput
from rushtracker.models import Rush, UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from rushtracker.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit, Hidden
from django import forms
from django.core.urlresolvers import reverse


class DetailForm(ModelForm):

    class Meta:
        model = Rush
        widgets = {
            'rush_contacted_date': DateInput(attrs={'type': 'date'})}
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Update', css_class='btn-primary'))

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 
            'email', 'password1', 'password2')
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(UserForm, self).save(commit=True)
        user_profile = UserProfile(user=user)
        user_profile.save()
        return user, user_profile


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

class AuthenticationFormAny(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthenticationFormAny, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.render_hidden_fields = True
        self.helper.form_tag = False
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn_primary'))

