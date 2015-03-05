from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django.forms import DateInput, ModelForm, Textarea
from events.models import Event


class CreateEventForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CreateEventForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper.layout = Layout(
            Field('title'),
            # TODO: maybe add description field
            # Field('description', widget='description', required=False),
            Field('date', css_class='datepicker'),
            # TODO: should attendance be part of this create form?
            Field('attendance', required=False),
            Submit('submit', 'Submit', css_class='btn-primary'))

    class Meta:
        model = Event

        widgets = {
          'description': Textarea(attrs={'rows':4, 'cols':1}),
          'event_date': DateInput(attrs={'type': 'date'})
        }
