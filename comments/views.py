from rushtracker.models import Rush
from comments.models import Comment
from comments.forms import CreateCommentForm
from django.shortcuts import get_object_or_404
from django.views import generic
from braces.views import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse
import pdb


class CommentListView(LoginRequiredMixin, generic.ListView):
    template_name = 'comments/comment_list.html'
    context_object_name = 'rush_comments'

    def get_queryset(self):
        self.rush = get_object_or_404(Rush, pk=self.kwargs['pk'])
        return Comment.objects.filter(rush=self.rush).order_by('created_at')

    def get_context_data(self):
        context = super(CommentListView, self).get_context_data()
        context['profile_picture'] = self.rush.picture
        context['CommentForm'] = CreateCommentForm(initial={'rush': self.kwargs['pk'], 'user': self.request.user}, request=self.request)
        return context
	def get_form_kwargs(self):
		kwargs = super(CommentListView, self).get_form_kwargs()
		kwargs['request'] = self.request
		return kwargs
class CommentCreationView(LoginRequiredMixin, generic.CreateView):
	model = Comment
	form_class = CreateCommentForm
	def form_invalid(self, form):
		return JsonResponse({
			'success':False,
			'errors': dict(form.errors.items()),
			})
	def form_valid(self, form):
		print "hello"
		if self.request.user.has_perm('chapter_admin') is False:
			print "false"
			#this should realistically probably be in the form 
			form.cleaned_data['user'] = self.request.user
			#maybe call is valid here again?? 
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
	def post(self, request, *args, **kwargs):
		request.POST = request.POST.copy()
		if request.user.has_perm('authentication.chapter_admin') is False:
			request.POST['user'] = request.user.id

		form = CreateCommentForm(request.POST, request=self.request)
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)
	#def post(self, request, *args, **kwargs):
		