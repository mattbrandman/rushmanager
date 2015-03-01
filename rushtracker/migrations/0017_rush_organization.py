# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
        ('rushtracker', '0016_auto_20150228_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='rush',
            name='organization',
            field=models.ForeignKey(default=0, to='organization.Organization'),
            preserve_default=False,
        ),
    ]
