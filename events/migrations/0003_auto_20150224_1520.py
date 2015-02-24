# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20150224_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendance',
            field=models.ManyToManyField(to='rushtracker.Rush', null=True, blank=True),
            preserve_default=True,
        ),
    ]
