from rushtracker.models import Rush
from comments.models import Comment
from comments.forms import CreateCommentForm, CreateCommentFormAdmin
from django.shortcuts import get_object_or_404
from django.views import generic
from braces.views import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse
from authentication.mixins import CorrectOrganizationMixin
from django.forms.models import modelform_factory
from django.contrib.auth.models import User


class CommentListView(LoginRequiredMixin, CorrectOrganizationMixin, generic.ListView):
    template_name = 'comments/comment_list.html'
    context_object_name = 'rush_comments'
    def dispatch(self, request, *args, **kwargs):
		self.organization = get_object_or_404(Rush, pk=kwargs['pk']).organization
		return super(CommentListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        self.rush = get_object_or_404(Rush, pk=self.kwargs['pk'])
        return Comment.objects.filter(rush=self.rush).order_by('created_at')

    def get_context_data(self):
        context = super(CommentListView, self).get_context_data()
        context['profile_picture'] = self.rush.picture
        if not self.request.user.has_perm('authentication.chapter_admin'):
        	context['CommentForm'] = CreateCommentForm(initial={'rush': self.kwargs['pk']}, request=self.request)
        else: 
        	context['CommentForm'] = CreateCommentFormAdmin(initial={'rush': self.kwargs['pk']}, request=self.request)
        	context['CommentForm'].fields['user'].queryset = User.objects.filter(organization=self.request.user.profile.organization)
        return context

	def get_form_kwargs(self):
		kwargs = super(CommentListView, self).get_form_kwargs()
		kwargs['request'] = self.request
		return kwargs
        
class CommentCreationView(LoginRequiredMixin, generic.CreateView):
	model = Comment

	#gives correct form based on user permission
	def get_form_class(self):
		if self.request.user.has_perm('authentication.chapter_admin'):
			print "here"
			return CreateCommentFormAdmin
		else:
			return CreateCommentForm

	def form_invalid(self, form):
		return JsonResponse({
			'success':False,
			'errors': dict(form.errors.items()),
			})

	def form_valid(self, form):
		self.object = form.save()
		return JsonResponse({
			'success':True,
			'username': self.object.user.username,
			'comment': self.object.comment,
		})

	def get_form_kwargs(self):
		kwargs = super(CommentCreationView, self).get_form_kwargs()
		kwargs['request'] = self.request
		return kwargs
