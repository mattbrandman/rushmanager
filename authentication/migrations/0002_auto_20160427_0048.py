# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushperiod', '0001_initial'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active_rush_period', models.ForeignKey(blank=True, to='rushperiod.RushPeriod', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='brotheruser',
            name='settings',
            field=models.ForeignKey(blank=True, to='authentication.Settings', null=True),
        ),
    ]
