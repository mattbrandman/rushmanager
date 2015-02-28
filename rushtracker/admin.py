from django.contrib import admin
from rushtracker.models import Rush
from authentication.models import UserProfile

class RushInLine(admin.StackedInline):
	model = Rush
	extra = 3
admin.site.register(Rush)
admin.site.register(UserProfile)
