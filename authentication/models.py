from django.db import models
from django.contrib.auth.models import User
from organization.models import Organization
from django.contrib.auth.models import Permission
from rushtracker.models import Base


class UserProfile(Base):
	user = models.OneToOneField(User, related_name="profile")
	class Meta:
		permissions = (
			("chapter_admin", "Can access chapter admin page"),
		)
	def __str__(self):
		return self.user.username