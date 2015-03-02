from django.db import models
from django.contrib.auth.models import User
import uuid

class Organization(models.Model):
	owner = models.ForeignKey(User)
	national_organization = models.CharField(max_length=500)
	chapter_name = models.CharField(max_length=500)
	def __str__(self):
		return self.national_organization + ' ' + self.chapter_name

