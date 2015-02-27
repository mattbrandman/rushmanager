from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div
from django.forms import DateInput, ModelForm, Textarea
from comments.models import Comment

class CreateCommentForm(ModelForm):
    success_url = '.'

    def __init__(self, *args, **kwargs):
            super(CreateCommentForm, self).__init__(*args, **kwargs)

            self.helper = FormHelper(self)

            self.helper.layout = Layout(
                Div(
                    Div(
                        Field('user'),
                        Field('event'),
                        css_class="span4",
                        ),
                    Div(
                        Field('comment'),
                        css_class="span8",
                    ),
                    css_class="container-fluid",
                ),
                Submit('submit', 'Submit', css_class='btn-primary'))

    class Meta:
        model = Comment