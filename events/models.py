from django.db import models
from rushtracker.models import Rush
from organization.models import Organization
class Event(models.Model):
    title = models.CharField('Event Title', max_length=200)
    description = models.CharField(max_length=2000, blank=True, null=True)
    date = models.DateField('Event Date')
    attendance = models.ManyToManyField(Rush, blank=True, null=True)
    organization = models.ForeignKey(Organization)

    def __str__(self):
        return self.title