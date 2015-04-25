# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_organization_active_rush_period'),
        ('ranking', '0004_ranking_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ranking',
            name='organization',
            field=models.ForeignKey(default=1, to='organization.Organization'),
            preserve_default=False,
        ),
    ]
