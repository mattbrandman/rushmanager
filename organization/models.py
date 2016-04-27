from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from tenant_schemas.models import TenantMixin
import uuid

class Organization(TenantMixin):
	national_organization = models.CharField(max_length=500)
	chapter_name = models.CharField(max_length=500)
	#lazy import to prevent circular imports

	auto_create_schema = True
	def __str__(self):
		return self.national_organization + ' ' + self.chapter_name