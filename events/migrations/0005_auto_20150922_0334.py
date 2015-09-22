# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushperiod', '0001_initial'),
        ('events', '0004_auto_20150910_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='attendance',
        ),
        migrations.AddField(
            model_name='event',
            name='rush_period',
            field=models.ForeignKey(blank=True, to='rushperiod.RushPeriod', null=True),
        ),
    ]
