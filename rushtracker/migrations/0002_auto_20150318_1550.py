# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0001_squashed_0022_auto_20150310_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rush',
            name='organization',
            field=models.ForeignKey(to='organization.Organization'),
            preserve_default=True,
        ),
    ]
