# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0007_auto_20150709_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rush',
            name='picture',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
