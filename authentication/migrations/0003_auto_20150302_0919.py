# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20150302_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='organization',
            field=models.OneToOneField(null=True, blank=True, to='organization.Organization'),
            preserve_default=True,
        ),
    ]
