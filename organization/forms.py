
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import DateInput, ModelForm, Textarea
from organization.models import Organization
from django.db import models
from django.contrib.auth.models import User

class CreateOrganizationForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CreateOrganizationForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

	class Meta:
		model = Organization
		fields = ('owner', 'national_organization', 'chapter_name')