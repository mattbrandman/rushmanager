from django.db import models
from rushtracker.models import Rush
from organization.models import Organization
from tenancy.models import TenantAware
from rushperiod.models import RushPeriod
class Event(TenantAware):
    title = models.CharField('Event Title', max_length=200)
    description = models.CharField(max_length=2000, blank=True, null=True)
    date = models.DateField('Event Date')
    organization = models.ForeignKey(Organization)
    rush_period = models.ForeignKey(RushPeriod, null=True, blank=True)
    attendance = models.ManyToManyField(Rush, null=True, blank=True)
    def __str__(self):
        return self.title