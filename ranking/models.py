from django.db import models
from rushtracker.models import Rush
class Ranking(models.Model):
	rush = models.ForeignKey(Rush)
	rank = models.IntegerField()

