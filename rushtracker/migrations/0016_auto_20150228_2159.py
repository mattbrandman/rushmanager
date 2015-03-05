# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0015_auto_20150228_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rush',
            name='picture_link',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Picture Link', blank=True),
            preserve_default=True,
        ),
    ]
