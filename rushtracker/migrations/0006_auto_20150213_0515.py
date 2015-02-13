# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0005_userprofile_rand_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rush',
            name='rush_email_address',
            field=models.EmailField(max_length=100),
            preserve_default=True,
        ),
    ]
