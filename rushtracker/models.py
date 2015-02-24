from django.db import models
from django.contrib.auth.models import User
class Rush(models.Model):
	name = models.CharField('Name', max_length=200)
	contact = models.ForeignKey(User, verbose_name='Brotherhood Contact', limit_choices_to={'is_staff': False}, blank=True, null=True)
	number = models.CharField('Phone Number', max_length=30)
	facebook_link = models.CharField('FaceBook Link', max_length = 200)
	contacted_date = models.DateField('Date Contacted')
	email_address = models.EmailField('Email Address', max_length=100)
	rank = models.IntegerField('Rank', default = 5)
	
	def __str__(self):
		return self.name

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	rand_text = models.CharField(max_length=20)
	def __str__(self):
		return self.user.username