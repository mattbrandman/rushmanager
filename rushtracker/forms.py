from django.forms import ModelForm, DateInput
from rushtracker.models import Rush

class DetailForm(ModelForm):
	class Meta:
		model = Rush
		widgets = {
			'rush_contacted_date' : DateInput(attrs={'type' : 'date'})}