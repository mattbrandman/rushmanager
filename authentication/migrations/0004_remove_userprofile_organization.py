# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20150302_0919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='organization',
        ),
    ]
