# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comment_event'),
        ('rushperiod', '0001_initial'),
        ('rushtracker', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='organization',
            field=models.ForeignKey(to='organization.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='rush',
            field=models.ForeignKey(to='rushtracker.Rush'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='rush_period',
            field=models.ForeignKey(to='rushperiod.RushPeriod'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
