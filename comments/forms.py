from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django.forms import DateInput, ModelForm, Textarea
from comments.models import Comment

class CreateCommentForm(ModelForm):
    success_url = '.'

    def __init__(self, *args, **kwargs):
            super(CreateCommentForm, self).__init__(*args, **kwargs)

            self.helper = FormHelper(self)

            self.helper.layout = Layout(
                Field('user'),
                Field('comment'),
                Field('event'),
                Submit('submit', 'Submit', css_class='btn-primary'))

    class Meta:
        model = Comment