from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div
from django.forms import DateInput, ModelForm, Textarea
from comments.models import Comment

class CreateCommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
            super(CreateCommentForm, self).__init__(*args, **kwargs)

            self.helper = FormHelper(self)
            self.helper.layout = Layout(
                Div(
                    Div(
                        Field('rush'),
                        Field('user'),
                        Field('event'),
                        css_class="col-md-4",
                        ),
                    Div(
                        Field('comment'),
                        css_class="col-md-8",
                    ),
                    css_class="row",
                ),
                Submit('submit', 'Submit', css_class='btn-primary'))

    class Meta:
        model = Comment