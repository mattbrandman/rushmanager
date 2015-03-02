# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20150301_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='join_token',
        ),
    ]
