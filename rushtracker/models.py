from django.db import models
from django.contrib.auth.models import User
class Brother(models.Model):
	brother_name = models.CharField(max_length = 200)
	brother_year = models.IntegerField(default = 1)
	brother_years_in_fraternity = models.IntegerField(default = 1)

	def __str__(self):
		return self.brother_name


class Rush(models.Model):
	rush_name = models.CharField(max_length=200)
	rush_contact = models.ForeignKey(Brother)
	rush_number = models.CharField(max_length=30)
	rush_facebook_link = models.CharField(max_length = 200)
	rush_contacted_date = models.DateField('Date Contacted')
	rush_email_address = models.CharField(max_length=100)
	rush_rank = models.IntegerField(default = 5)
	
	def __str__(self):
		return self.rush_name

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	def __str__(self):
		return self.user.username