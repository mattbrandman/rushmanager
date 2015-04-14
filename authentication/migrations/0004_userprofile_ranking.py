# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields.hstore


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20150409_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='ranking',
            field=django.contrib.postgres.fields.hstore.HStoreField(null=True, blank=True),
        ),
    ]
