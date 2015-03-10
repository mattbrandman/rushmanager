# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushperiod', '0001_initial'),
        ('rushtracker', '0020_remove_rush_rush_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='rush',
            name='rushperiod',
            field=models.ManyToManyField(to='rushperiod.RushPeriod'),
            preserve_default=True,
        ),
    ]
