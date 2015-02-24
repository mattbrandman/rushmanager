# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0006_auto_20150224_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rush',
            name='contact',
            field=models.ForeignKey(verbose_name=b'Brotherhood Contact', blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
