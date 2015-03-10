# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0021_rush_rushperiod'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rush',
            old_name='rushperiod',
            new_name='rush_period',
        ),
    ]
