# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0003_auto_20150416_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rush',
            name='rating',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
