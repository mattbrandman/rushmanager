# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_remove_organization_join_token'),
        ('authentication', '0004_remove_userprofile_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='organization',
            field=models.OneToOneField(default=1, to='organization.Organization'),
            preserve_default=False,
        ),
    ]
