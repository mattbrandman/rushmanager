from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django.forms import DateInput, ModelForm, Textarea
from events.models import Event


class CreateEventForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateEventForm, self).__init__(*args, **kwargs)

        widgets = {
          'description': Textarea(attrs={'rows':4, 'cols':1}),
        }

        self.helper = FormHelper(self)
        self.helper['contacted_date'].wrap(Field, css_class="datepicker")
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

        self.helper.layout = Layout(
            Field('title'),
            Field('description', widget='description'),
            Field('date'),
            Field('attendance'))

    class Meta:
        model = Event
