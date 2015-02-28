# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0011_auto_20150228_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rush',
            name='first_name',
            field=models.CharField(max_length=200, verbose_name=b'First Name'),
            preserve_default=True,
        ),
    ]
