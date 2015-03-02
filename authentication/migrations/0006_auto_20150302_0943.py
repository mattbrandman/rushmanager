# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_userprofile_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='organization',
            field=models.ForeignKey(to='organization.Organization'),
            preserve_default=True,
        ),
    ]
