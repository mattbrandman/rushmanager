from django.db import models
from organization.models import Organization
class RushPeriod(models.Model):
	name = models.CharField(max_length=200)
	start_date = models.DateField()
	end_date = models.DateField()
	def __str__(self):
		return self.name