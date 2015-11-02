# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0008_auto_20151028_2222'),
        ('events', '0005_auto_20150922_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendance',
            field=models.ManyToManyField(to='rushtracker.Rush', null=True, blank=True),
        ),
    ]
