# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0005_auto_20150223_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'Event Title')),
                ('description', models.CharField(max_length=2000)),
                ('date', models.DateField(verbose_name=b'Event Date')),
                ('attendance', models.ManyToManyField(to='rushtracker.Rush')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
