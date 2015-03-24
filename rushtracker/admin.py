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
admin.site.register(Rush, RushAdmin)
