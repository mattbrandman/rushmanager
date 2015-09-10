from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django.forms import DateInput, ModelForm, Textarea
from events.models import Event
from django.contrib.auth import get_user_model
from rushtracker.models import Rush
from django.http import HttpResponseForbidden


class CreateEventForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CreateEventForm, self).__init__(*args, **kwargs)
        self.fields['attendance'].queryset = Rush.tenant_objects.all()
        self.helper = FormHelper(self)

        self.helper.layout = Layout(
            Field('title', required=False),
            # TODO: maybe add description field
            Field('description'),

            Field('date', css_class='datepicker'),
            # TODO: should attendance be part of this create form?
            Field('attendance'),
            Submit('submit', 'Submit', css_class='btn-primary'))
    def save(self):
        if not self.request.user.has_perm('authentication.chapter_admin'):
            return HttpResponseForbidden
        else:
            event = super(CreateEventForm, self).save(commit=False)
            event.organization = self.request.user.organization
            event.save()
            return event
    class Meta:
        model = Event
        exclude = ['organization']

        widgets = {
          'description': Textarea(attrs={'rows':4, 'cols':1}),
          'event_date': DateInput(attrs={'type': 'date'})
        }
