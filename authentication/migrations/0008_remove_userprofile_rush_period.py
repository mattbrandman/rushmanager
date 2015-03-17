# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_userprofile_rush_period'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='rush_period',
        ),
    ]
