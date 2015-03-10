# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushperiod', '0001_initial'),
        ('rushtracker', '0018_rush_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rush',
            name='picture_link',
        ),
        migrations.AddField(
            model_name='rush',
            name='rush_period',
            field=models.ForeignKey(default=5, to='rushperiod.RushPeriod'),
            preserve_default=False,
        ),
    ]
