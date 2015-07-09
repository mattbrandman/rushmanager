# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0006_auto_20150518_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rush',
            name='organization',
            field=models.ForeignKey(to='organization.Organization', blank=True),
        ),
    ]
