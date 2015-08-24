from django.contrib import admin
from authentication.models import UserProfile
from authentication.models import BrotherUser

class BrotherUserAdmin(admin.ModelAdmin):
	def get_queryset(self, request):
		return BrotherUser.admin.all()

admin.site.register(UserProfile)
admin.site.register(BrotherUser, BrotherUserAdmin)