from django.db import models
from django.contrib.auth.models import User
from organization.models import Organization
from rushperiod.models import RushPeriod
from django.conf import settings
from tenancy.models import TenantAware

class Rush(TenantAware):
	first_name = models.CharField('First Name', max_length=200, blank=False )
	last_name = models.CharField('Last Name', max_length=200, blank=True, null=True )
	primary_contact = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Brotherhood Contact', blank=True, null=True, related_name='primary_contact_set')
	secondary_contact = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Secondary Brotherhood Contact', blank=True, null=True, related_name='secondary_contact_set')
	phone_number = models.CharField('Phone Number', max_length=30, blank=True, null=True)
	facebook_link = models.CharField('FaceBook Link', max_length = 200, blank=True, null=True)
	contacted_date = models.DateField('Date Contacted', blank=True, null=True)
	email_address = models.EmailField('Email Address', max_length=100, blank=True, null=True)
	rank = models.IntegerField('Rank', default = 5, blank=True, null=True)
	dorm = models.CharField('Dorm', max_length=200, blank=True, null=True)
	picture = models.ImageField(upload_to='profile_picture', blank=True, null=True)
	rush_period = models.ManyToManyField(RushPeriod)
	organization = models.ForeignKey(Organization, blank=True)
	graduating_year = models.IntegerField(blank=True, null=True)
	is_available = models.BooleanField('Is Available To Rush', default=True)
	is_legacy = models.BooleanField('Legacy', default=False)


	def __str__(self):
		return self.first_name + " " + self.last_name
