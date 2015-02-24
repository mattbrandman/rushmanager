from django.forms import ModelForm

class CreateEventForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreateEventForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Event
