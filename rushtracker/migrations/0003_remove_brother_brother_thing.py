# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0002_brother_brother_thing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brother',
            name='brother_thing',
        ),
    ]
