# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushperiod', '0001_initial'),
        ('authentication', '0006_auto_20150302_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='rush_period',
            field=models.ManyToManyField(to='rushperiod.RushPeriod'),
            preserve_default=True,
        ),
    ]
