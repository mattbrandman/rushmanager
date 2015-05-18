# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0004_auto_20150416_2225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rush',
            name='rating',
        ),
        migrations.AddField(
            model_name='rush',
            name='is_legacy',
            field=models.BooleanField(default=False, verbose_name=b'Legacy'),
        ),
    ]
