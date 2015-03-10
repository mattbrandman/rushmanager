from django.db import models
from django.contrib.auth.models import User
from organization.models import Organization
from rushperiod.models import RushPeriod
class Rush(Base):
	first_name = models.CharField('First Name', max_length=200, blank=False )
	last_name = models.CharField('Last Name', max_length=200, blank=True, null=True )
	primary_contact = models.ForeignKey(User, verbose_name='Brotherhood Contact', blank=True, null=True, related_name='primary_contact_set')
	secondary_contact = models.ForeignKey(User, verbose_name='Secondary Brotherhood Contact', blank=True, null=True, related_name='secondary_contact_set')
	phone_number = models.CharField('Phone Number', max_length=30, blank=True, null=True)
	facebook_link = models.CharField('FaceBook Link', max_length = 200, blank=True, null=True)
	contacted_date = models.DateField('Date Contacted', blank=True, null=True)
	email_address = models.EmailField('Email Address', max_length=100, blank=True, null=True)
	rank = models.IntegerField('Rank', default = 5, blank=True, null=True)
	dorm = models.CharField('Dorm', max_length=200, blank=True, null=True)
	picture = models.ImageField(upload_to='profile_picture', blank=True, null=True)
	
	def __str__(self):
		return self.first_name + " " + self.last_name

class Base(models.Model):
	rush_period = models.ManyToManyField(RushPeriod)
	organization = models.ForeignKey(Organization)
	class Meta:
		abstract = True
