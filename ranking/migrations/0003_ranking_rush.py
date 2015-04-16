# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0003_auto_20150416_1603'),
        ('ranking', '0002_auto_20150416_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='ranking',
            name='rush',
            field=models.ForeignKey(default=1, to='rushtracker.Rush'),
            preserve_default=False,
        ),
    ]
