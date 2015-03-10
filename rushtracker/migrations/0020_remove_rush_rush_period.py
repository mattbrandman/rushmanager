# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0019_auto_20150310_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rush',
            name='rush_period',
        ),
    ]
