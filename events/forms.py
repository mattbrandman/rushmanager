from django.forms import ModelForm
from events.models import Event

class CreateEventForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateEventForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Event
