from django.db import models
from middleware import get_current_user

class TenantManager(models.Manager):
	def get_queryset(self):
		return super(TenantManager, self).get_queryset().filter(organization=get_current_user().organization)

class TenantAware(models.Model):
	objects = models.Manager()
	tenant_objects = TenantManager()
	class Meta:
		abstract = True