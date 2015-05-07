# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20150505_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='active_rush_period',
            field=models.ForeignKey(related_name='active_period_organization', blank=True, to='rushperiod.RushPeriod', null=True),
        ),
    ]
