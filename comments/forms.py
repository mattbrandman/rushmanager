from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div, HTML, Hidden
from django.forms import DateInput, ModelForm, Textarea
from comments.models import Comment

class CreateCommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CreateCommentForm, self).__init__(*args, **kwargs)
        #this can and should be better TODO
        #Exclude will override the layout even if it's explicit
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Div(
                    Field('event'),
                    css_class="col-md-8",
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
        exclude = ['user', 'organization']
    def save(self, commit=True):
        comment = super(CreateCommentForm, self).save(commit=False)
        comment.user = self.request.user
        comment.organization = self.request.user.profile.organization
        comment.save()


class CreateCommentFormAdmin(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        print self.request
        super(CreateCommentFormAdmin, self).__init__(*args, **kwargs)
        #this can and should be better TODO
        #Exclude will override the layout even if it's explicit
        self.helper = FormHelper(self)
        if not self.request.user.has_perm('authentication.chapter_admin'):
            self.helper.layout = Layout(
                Div(
                    Div(
                        Field('user'),
                        css_class="col-md-4"),
                    Div(
                        Field('event'),
                        css_class="col-md-4"),
                    Div(
                        Field('comment'),
                        css_class="col-md-8",
                    ),
                css_class="row",
            ),
            Field('rush', type="hidden"),
            Submit('submit', 'Submit', css_class='btn-primary'))
    def save(self, commit=True):
        comment = super(CreateCommentForm, self).save(commit=False)
        comment.organization = self.request.user.profile.organization
        comment.save()
    class Meta:
        #if user has chapter admin privileges exclude nothing
        #if they don't exclude the user field
        model = Comment
        fields = ['user', 'event', 'comment', 'rush']



