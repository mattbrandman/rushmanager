# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_auto_20150506_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='active_rush_period',
            field=models.ForeignKey(related_name='active_period_organization', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='rushperiod.RushPeriod', null=True),
        ),
    ]
