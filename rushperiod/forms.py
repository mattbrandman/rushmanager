from django import forms
from rushperiod.models import RushPeriod
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Hidden
from braces.forms import UserKwargModelFormMixin
class CreateRushPeriodForm(UserKwargModelFormMixin, forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CreateRushPeriodForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper['start_date'].wrap(Field, css_class="datepicker")
		self.helper['end_date'].wrap(Field, css_class="datepicker")
		self.helper.add_input(Submit('submit', 'Update', css_class='btn-primary'))
	class Meta:
		model = RushPeriod
		exclude = ['organization',]
	def save(self, commit=True):
		if not commit:
			raise NotImplementedError("Can't create Rush Period without database save")
		my_rush_period = super(CreateRushPeriodForm, self).save(commit=False)
		my_rush_period.organization = self.user.organization
		organization = my_rush_period.organization
		my_rush_period.save()
		organization.active_rush_period = my_rush_period
		organization.save()