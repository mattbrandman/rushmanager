# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='join_token',
            field=models.CharField(default=uuid.uuid1, unique=True, max_length=40),
            preserve_default=True,
        ),
    ]
