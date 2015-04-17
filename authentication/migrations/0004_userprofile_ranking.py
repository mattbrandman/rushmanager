# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0003_ranking_rush'),
        ('authentication', '0003_auto_20150409_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='ranking',
            field=models.ManyToManyField(to='ranking.Ranking'),
        ),
    ]
