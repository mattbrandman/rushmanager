from django.contrib import admin
from authentication.models import UserProfile
from authentication.models import BrotherUser

admin.site.register(UserProfile)
admin.site.register(BrotherUser)