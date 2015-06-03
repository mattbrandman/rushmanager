# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_remove_userprofile_ranking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brotheruser',
            name='first_name',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='brotheruser',
            name='last_name',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
