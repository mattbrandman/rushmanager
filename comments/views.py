class CommentView(LoginRequiredMixin, generic.ListView):
    template_name = 'comments/comment_list.html'
    context_object_name = 'rush_comments'

    def get_queryset(self):
        return Comment.objects.filter(rush=)