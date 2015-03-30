# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('auth', '0001_initial'),
        ('organization', '0002_organization_active_rush_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='brotheruser',
            name='organization',
            field=models.ForeignKey(to='organization.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brotheruser',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
            preserve_default=True,
        ),
    ]
