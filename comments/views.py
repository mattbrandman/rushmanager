from rushtracker.models import Rush
from comments.models import Comment
from comments.forms import CreateCommentForm
from django.shortcuts import get_object_or_404
from django.views import generic
from braces.views import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse


class CommentListView(LoginRequiredMixin, generic.ListView):
    template_name = 'comments/comment_list.html'
    context_object_name = 'rush_comments'

    def get_queryset(self):
        self.rush = get_object_or_404(Rush, pk=self.kwargs['pk'])
        return Comment.objects.filter(rush=self.rush)

    def get_context_data(self):
        context = super(CommentListView, self).get_context_data()
        context['CommentForm'] = CreateCommentForm
        context['rushKey'] = self.kwargs['pk']
        return context
class CommentCreationView(LoginRequiredMixin, generic.CreateView):
	model = Comment
	def form_invalid(self, form):
		return JsonResponse({
			'success':False,
			'errors': dict(form.errors.items()),
			})
	def form_valid(self, form):
		self.object = form.save()
		return JsonResponse({
			'username': self.object.user.username,
			'comment': self.object.comment,
		})