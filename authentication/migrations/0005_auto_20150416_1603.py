# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0002_auto_20150416_1603'),
        ('authentication', '0004_userprofile_ranking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='ranking',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ranking',
            field=models.ManyToManyField(to='ranking.Ranking'),
        ),
    ]
