from django.forms import ModelForm, DateInput, PasswordInput
from rushtracker.models import Rush, UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from rushtracker.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class DetailForm(ModelForm):
	class Meta:
		model = Rush
		widgets = {
			'rush_contacted_date' : DateInput(attrs={'type' : 'date'})}
	helper = FormHelper();
	helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')
	helper = FormHelper();
	helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))


class UserProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
	helper = FormHelper();
	helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
