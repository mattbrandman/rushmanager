import datetime

from django.contrib.auth.models import User
from django.utils import timezone
from events.models import Event
from rushtracker.models import Rush
from rushperiod.models import RushPeriod
from organization.models import Organization
from django.conf import settings

from django.db import models

class Comment(models.Model):

    rush = models.ForeignKey(Rush)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    event = models.ForeignKey(Event, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    comment = models.TextField()
    organization = models.ForeignKey(Organization)
    rush_period = models.ForeignKey(RushPeriod)


    # TODO: I want to be able to have the option of having a positve or negative comment.
    # not sure the best way to do this but I think it should be something like below
    '''
    comment_opinon = models.CharField(choices=OPINION_CHOICES, default=0)

     OPINION_CHOICES = (
        ('-1', 'Netgative',),
        ('0', 'Neutral',),
        ('1', 'Postive',),
    )
    '''
    def __str__(self):
        return "" + self.user.username + "'s comment on " + self.rush.first_name
