# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20150318_1614'),
        ('events', '0002_event_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='organization',
            field=models.ForeignKey(default=1, to='organization.Organization'),
            preserve_default=False,
        ),
    ]
