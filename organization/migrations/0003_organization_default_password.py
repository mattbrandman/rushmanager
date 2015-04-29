# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_organization_active_rush_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='default_password',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
