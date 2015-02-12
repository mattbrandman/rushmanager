from django.contrib import admin
from rushtracker.models import Rush, Brother, UserProfile

class RushInLine(admin.StackedInline):
	model = Rush
	extra = 3
class BrotherAdmin(admin.ModelAdmin):
	inlines = [RushInLine]
admin.site.register(Brother, BrotherAdmin)
admin.site.register(Rush)
admin.site.register(UserProfile)
