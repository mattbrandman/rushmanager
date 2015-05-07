# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_organization_default_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='active_rush_period',
            field=models.OneToOneField(related_name='active_period_organization', null=True, blank=True, to='rushperiod.RushPeriod'),
        ),
    ]
