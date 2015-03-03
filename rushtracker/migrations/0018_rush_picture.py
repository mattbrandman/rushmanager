# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0017_rush_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='rush',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'profile_picture', blank=True),
            preserve_default=True,
        ),
    ]
