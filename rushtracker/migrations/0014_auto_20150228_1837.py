# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rushtracker', '0013_rush_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rush',
            old_name='number',
            new_name='phone_number',
        ),
        migrations.RemoveField(
            model_name='rush',
            name='contact',
        ),
        migrations.AddField(
            model_name='rush',
            name='dorm',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Dorm', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rush',
            name='facebook_profile_pciture',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Profile Picture', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rush',
            name='primary_contact',
            field=models.ForeignKey(related_name='primary_contact_set', verbose_name=b'Brotherhood Contact', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rush',
            name='secondary_contact',
            field=models.ForeignKey(related_name='secondary_contact_set', verbose_name=b'Secondary Brotherhood Contact', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
