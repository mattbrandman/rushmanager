# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_remove_organization_join_token'),
        ('rushperiod', '0001_initial'),
        ('comments', '0002_auto_20150228_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='organization',
            field=models.ForeignKey(default=1, to='organization.Organization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='rush_period',
            field=models.ManyToManyField(to='rushperiod.RushPeriod'),
            preserve_default=True,
        ),
    ]
