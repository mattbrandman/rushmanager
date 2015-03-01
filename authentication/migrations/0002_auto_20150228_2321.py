# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='rand_text',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='organization',
            field=models.ForeignKey(default=0, to='organization.Organization'),
            preserve_default=False,
        ),
    ]
