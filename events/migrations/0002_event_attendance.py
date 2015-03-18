# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendance',
            field=models.ManyToManyField(to='rushtracker.Rush', null=True, blank=True),
            preserve_default=True,
        ),
    ]
