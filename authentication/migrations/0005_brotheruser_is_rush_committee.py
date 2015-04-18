# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_userprofile_ranking'),
    ]

    operations = [
        migrations.AddField(
            model_name='brotheruser',
            name='is_rush_committee',
            field=models.BooleanField(default=False),
        ),
    ]
