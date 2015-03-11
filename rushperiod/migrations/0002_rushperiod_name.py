# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushperiod', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rushperiod',
            name='name',
            field=models.CharField(default='spring', max_length=200),
            preserve_default=False,
        ),
    ]
