# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushperiod', '0002_rushperiod_name'),
        ('comments', '0004_remove_comment_rush_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rush_period',
            field=models.ForeignKey(default=3, to='rushperiod.RushPeriod'),
            preserve_default=False,
        ),
    ]
