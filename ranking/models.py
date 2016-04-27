from django.db import models
from rushtracker.models import Rush
from django.conf import settings
from organization.models import Organization
class Ranking(models.Model):
	rush = models.ForeignKey(Rush)
	rank = models.IntegerField()
	user = models.ForeignKey(settings.AUTH_USER_MODEL)

