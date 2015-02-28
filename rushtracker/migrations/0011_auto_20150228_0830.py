# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0010_auto_20150228_0259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rush',
            name='name',
        ),
        migrations.AddField(
            model_name='rush',
            name='first_name',
            field=models.CharField(default='Bob', max_length=200, verbose_name=b'First_Name'),
            preserve_default=False,
        ),
    ]
