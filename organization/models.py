from django.db import models
from django.contrib.auth.models import User
import uuid

class Organization(models.Model):
	owner = models.ForeignKey(User)
	national_organization = models.CharField(max_length=500)
	chapter_name = models.CharField(max_length=500)
	#lazy import to prevent circular imports
	active_rush_period = models.ForeignKey('rushperiod.RushPeriod', blank=True, null=True, related_name='active_period_organization')
	def __str__(self):
		return self.national_organization + ' ' + self.chapter_name
		
