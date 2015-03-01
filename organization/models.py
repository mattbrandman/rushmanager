from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
	owner = models.ForeignKey(User)
	national_organization = models.CharField(max_length=500)
	chapter_name = models.CharField(max_length=500)
	join_token = models.CharField(max_length=500)


