# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0008_auto_20150224_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rush',
            name='contacted_date',
            field=models.DateField(null=True, verbose_name=b'Date Contacted', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rush',
            name='email_address',
            field=models.EmailField(max_length=100, null=True, verbose_name=b'Email Address', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rush',
            name='facebook_link',
            field=models.CharField(max_length=200, null=True, verbose_name=b'FaceBook Link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rush',
            name='number',
            field=models.CharField(max_length=30, null=True, verbose_name=b'Phone Number', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rush',
            name='rank',
            field=models.IntegerField(default=5, null=True, verbose_name=b'Rank', blank=True),
            preserve_default=True,
        ),
    ]
