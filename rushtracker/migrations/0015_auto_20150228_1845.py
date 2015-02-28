# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rushtracker', '0014_auto_20150228_1837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rush',
            old_name='facebook_profile_pciture',
            new_name='picture_link',
        ),
    ]
