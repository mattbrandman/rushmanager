# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_brotheruser_is_rush_committee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='ranking',
        ),
    ]
