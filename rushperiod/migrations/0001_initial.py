# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_remove_organization_join_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='RushPeriod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('organization', models.ForeignKey(to='organization.Organization')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
