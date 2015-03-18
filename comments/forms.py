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
        #TODO: check that rush being submitted to is in same organization
        Field('rush', type="hidden"),
        Submit('submit', 'Submit', css_class='btn-primary'))
    class Meta:
        #if user has chapter admin privileges exclude nothing
        #if they don't exclude the user field
        model = Comment
        exclude = ['user', 'organization', 'rush_period']
    def save(self, commit=True):
        comment = super(CreateCommentForm, self).save(commit=False)
        comment.user = self.request.user
        comment.rush_period = self.request.user.profile.organization.active_rush_period
        comment.organization = self.request.user.profile.organization
        comment.save()
        return comment


class CreateCommentFormAdmin(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        print self.request
        super(CreateCommentFormAdmin, self).__init__(*args, **kwargs)
        #this can and should be better TODO
        #Exclude will override the layout even if it's explicit
        self.helper = FormHelper(self)
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
    class Meta:
        #if user has chapter admin privileges exclude nothing
        #if they don't exclude the user field
        model = Comment
        fields = ['user', 'event', 'comment', 'rush']
        exclude = ['rush_period',]
    def save(self, commit=True):
        comment = super(CreateCommentFormAdmin, self).save(commit=False)
        comment.organization = self.request.user.profile.organization
        comment.rush_period = self.request.user.profile.organization.active_rush_period
        #comment is updated with correct key and everything!
        comment.save()
        return comment



