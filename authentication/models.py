from django.db import models


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	rand_text = models.CharField(max_length=20)
	def __str__(self):
		return self.user.username