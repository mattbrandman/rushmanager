from django.forms import ModelForm, DateInput
from rushtracker.models import Rush
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class DetailForm(ModelForm):
	class Meta:
		model = Rush
		widgets = {
			'rush_contacted_date' : DateInput(attrs={'type' : 'date'})}
	helper = FormHelper();
	helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))