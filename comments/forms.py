from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div, HTML, Hidden
from django.forms import DateInput, ModelForm, Textarea
from comments.models import Comment

class CreateCommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        #self.user = kwargs.pop('user', None)
        self.request = kwargs.pop('request', None)
        super(CreateCommentForm, self).__init__(*args, **kwargs)
        #this can and should be better TODO
        if self.request.user.has_perm('authentication.chapter_admin') is True:
            imageField = Field('user')
        else:
            imageField = Hidden('user', '')
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Div(
                    imageField,
                    Field('event'),
                    css_class="col-md-4",
                ),
                Div(
                    Field('comment'),
                    css_class="col-md-8",
                ),
            css_class="row",
        ),
        Field('rush', type="hidden"),
        Submit('submit', 'Submit', css_class='btn-primary'))
    class Meta:
        #if user has chapter admin privileges exclude nothing
        #if they don't exclude the user field
        model = Comment
        fields = '__all__'

