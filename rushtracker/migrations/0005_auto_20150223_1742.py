# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0004_auto_20150218_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rush',
            name='rush_contact',
            field=models.ForeignKey(verbose_name=b'Brotherhood Contact', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rush',
            name='rush_email_address',
            field=models.EmailField(max_length=100, verbose_name=b'Email Address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rush',
            name='rush_facebook_link',
            field=models.CharField(max_length=200, verbose_name=b'FaceBook Link'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rush',
            name='rush_name',
            field=models.CharField(max_length=200, verbose_name=b'Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rush',
            name='rush_number',
            field=models.CharField(max_length=30, verbose_name=b'Phone Number'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rush',
            name='rush_rank',
            field=models.IntegerField(default=5, verbose_name=b'Rank'),
            preserve_default=True,
        ),
    ]
