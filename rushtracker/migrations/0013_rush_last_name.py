# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0012_auto_20150228_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='rush',
            name='last_name',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Last Name', blank=True),
            preserve_default=True,
        ),
    ]
