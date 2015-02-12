# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0004_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='rand_text',
            field=models.CharField(default='hello', max_length=20),
            preserve_default=False,
        ),
    ]
