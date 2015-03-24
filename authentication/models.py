from django.db import models
from django.contrib.auth.models import User
from organization.models import Organization
from django.contrib.auth.models import Permission, AbstractBaseUser 
from django.utils import timezone
from django.db import connection
from django.conf import settings
class BrotherUser(AbstractBaseUser):
	email = models.CharField(max_length=100, unique=True)
	is_staff = models.BooleanField(default=False)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	date_created = models.DateTimeField(default=timezone.now, blank=True)
	USERNAME_FIELD = 'email'

class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile")
	organization = models.ForeignKey(Organization)
	class Meta:
		permissions = (
			("chapter_admin", "Can access chapter admin page"),
		)
	def __str__(self):
		return self.user.username

