from django.contrib import admin
from rushtracker.models import Rush
from authentication.models import UserProfile
from comments.models import Comment
from django.contrib.auth import forms


class CommentInline(admin.StackedInline):
	model = Comment
	extra = 1
class RushAdmin(admin.ModelAdmin):
	inlines = [
		CommentInline,
	]
	def get_queryset(self, request):
		return Rush.objects.all()
admin.site.register(Rush, RushAdmin)
