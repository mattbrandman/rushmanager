from django.contrib import admin
from authentication.models import UserProfile

admin.authentication.register(UserProfile)