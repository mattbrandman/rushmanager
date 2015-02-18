# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rush',
            name='rush_contact',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Brother',
        ),
    ]
