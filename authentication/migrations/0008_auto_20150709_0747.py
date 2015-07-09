# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20150520_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brotheruser',
            name='organization',
            field=models.ForeignKey(to='organization.Organization', blank=True),
        ),
    ]
