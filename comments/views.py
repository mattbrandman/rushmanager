from rushtracker.models import Rush
from comments.models import Comment
from django.shortcuts import get_object_or_404
from django.views import generic
from braces.views import LoginRequiredMixin


class CommentView(LoginRequiredMixin, generic.ListView):
    template_name = 'comments/comment_list.html'
    context_object_name = 'rush_comments'

    def get_queryset(self):
        self.rush = get_object_or_404(Rush, pk=self.kwargs['pk'])
        return Comment.objects.filter(rush=self.rush)