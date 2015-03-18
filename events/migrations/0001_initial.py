# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'Event Title')),
                ('description', models.CharField(max_length=2000, null=True, blank=True)),
                ('date', models.DateField(verbose_name=b'Event Date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
