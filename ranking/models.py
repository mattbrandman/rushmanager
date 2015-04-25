from django.db import models
from rushtracker.models import Rush
from django.conf import settings
from tenancy.models import TenantAware
from organization.models import Organization
class Ranking(TenantAware):
	organization = models.ForeignKey(Organization)
	rush = models.ForeignKey(Rush)
	rank = models.IntegerField()
	user = models.ForeignKey(settings.AUTH_USER_MODEL)

