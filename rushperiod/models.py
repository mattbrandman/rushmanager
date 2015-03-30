from django.db import models
from organization.models import Organization
from tenancy.models import TenantAware
class RushPeriod(TenantAware):
	name = models.CharField(max_length=200)
	start_date = models.DateField()
	end_date = models.DateField()
	organization = models.ForeignKey(Organization)
	def __str__(self):
		return self.name