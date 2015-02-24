from django.db import models
from rushmanager.models import Rush

class Event(models.model):
    title = models.CharField('Event Title', max_length=200)
    description = models.CharField(max_length=2000)
    date = models.DateField('Event Date')
    attendance = models.ManyToManyField(Rush)

    def __str__(self):
        return self.title