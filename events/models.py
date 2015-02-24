from django.db import models
from rushtracker.models import Rush

class Event(models.Model):
    title = models.CharField('Event Title', max_length=200)
    description = models.CharField(max_length=2000, blank=True, null=True)
    date = models.DateField('Event Date')
    attendance = models.ManyToManyField(Rush, blank=True, null=True)

    def __str__(self):
        return self.title