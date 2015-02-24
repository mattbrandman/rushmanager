import datetime

from django.contrib.auth.models import User
from django.utils import timezone
from events.models import Event
from rushtracker.models import Rush

from django.db import models

class Comment(models.Model):

    rush = models.ForeignKey(Rush)
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    comment = models.TextField()


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
