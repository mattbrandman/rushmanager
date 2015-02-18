from django.db import models
from django.contrib.auth.models import User
class Rush(models.Model):
	rush_name = models.CharField('Name', max_length=200)
	rush_contact = models.ForeignKey(User, verbose_name='Brotherhood Contact', limit_choices_to={'is_staff': False})
	rush_number = models.CharField('Phone Number', max_length=30)
	rush_facebook_link = models.CharField('FaceBook Link', max_length = 200)
	rush_contacted_date = models.DateField('Date Contacted')
	rush_email_address = models.EmailField('Email Address', max_length=100)
	rush_rank = models.IntegerField('Rank', default = 5)
	
	def __str__(self):
		return self.rush_name

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	rand_text = models.CharField(max_length=20)
	def __str__(self):
		return self.user.username