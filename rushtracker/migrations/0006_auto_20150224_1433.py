# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0005_auto_20150223_1742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rush',
            old_name='rush_contact',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='rush',
            old_name='rush_contacted_date',
            new_name='contacted_date',
        ),
        migrations.RenameField(
            model_name='rush',
            old_name='rush_email_address',
            new_name='email_address',
        ),
        migrations.RenameField(
            model_name='rush',
            old_name='rush_facebook_link',
            new_name='facebook_link',
        ),
        migrations.RenameField(
            model_name='rush',
            old_name='rush_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='rush',
            old_name='rush_number',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='rush',
            old_name='rush_rank',
            new_name='rank',
        ),
    ]
