from django.db import models
from organization.models import Organization
class RushPeriod(models.Model):
	start_date = models.DateField()
	end_date = models.DateField()
	organization = models.ForeignKey(Organization)
	
