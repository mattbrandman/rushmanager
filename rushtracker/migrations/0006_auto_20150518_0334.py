# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0005_auto_20150518_0326'),
    ]

    operations = [
        migrations.AddField(
            model_name='rush',
            name='graduating_year',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='rush',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name=b'Is Available To Rush'),
        ),
    ]
