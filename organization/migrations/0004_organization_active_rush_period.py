# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushperiod', '0002_rushperiod_name'),
        ('organization', '0003_remove_organization_join_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='active_rush_period',
            field=models.ForeignKey(related_name='active_period_organization', blank=True, to='rushperiod.RushPeriod', null=True),
            preserve_default=True,
        ),
    ]
