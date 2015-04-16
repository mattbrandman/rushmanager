# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0002_rush_ranking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rush',
            name='ranking',
        ),
        migrations.AddField(
            model_name='rush',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
