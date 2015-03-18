# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'rushtracker', '0001_initial'), (b'rushtracker', '0002_auto_20150218_0459'), (b'rushtracker', '0003_auto_20150218_1600'), (b'rushtracker', '0004_auto_20150218_1632'), (b'rushtracker', '0005_auto_20150223_1742'), (b'rushtracker', '0006_auto_20150224_0342'), (b'rushtracker', '0007_auto_20150224_1602'), (b'rushtracker', '0008_auto_20150224_1604'), (b'rushtracker', '0009_auto_20150224_2152'), (b'rushtracker', '0010_auto_20150228_0259'), (b'rushtracker', '0011_auto_20150228_0830'), (b'rushtracker', '0012_auto_20150228_0831'), (b'rushtracker', '0013_rush_last_name'), (b'rushtracker', '0014_auto_20150228_1837'), (b'rushtracker', '0015_auto_20150228_1845'), (b'rushtracker', '0016_auto_20150228_2143'), (b'rushtracker', '0017_rush_organization'), (b'rushtracker', '0018_rush_picture'), (b'rushtracker', '0019_auto_20150310_2306'), (b'rushtracker', '0020_remove_rush_rush_period'), (b'rushtracker', '0021_rush_rushperiod'), (b'rushtracker', '0022_auto_20150310_2346')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rushperiod', '0001_initial'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rush',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(max_length=30, null=True, verbose_name=b'Phone Number', blank=True)),
                ('facebook_link', models.CharField(max_length=200, null=True, verbose_name=b'FaceBook Link', blank=True)),
                ('contacted_date', models.DateField(null=True, verbose_name=b'Date Contacted', blank=True)),
                ('email_address', models.EmailField(max_length=100, null=True, verbose_name=b'Email Address', blank=True)),
                ('rank', models.IntegerField(default=5, null=True, verbose_name=b'Rank', blank=True)),
                ('first_name', models.CharField(max_length=200, verbose_name=b'First Name')),
                ('last_name', models.CharField(max_length=200, null=True, verbose_name=b'Last Name', blank=True)),
                ('dorm', models.CharField(max_length=200, null=True, verbose_name=b'Dorm', blank=True)),
                ('primary_contact', models.ForeignKey(related_name='primary_contact_set', verbose_name=b'Brotherhood Contact', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('secondary_contact', models.ForeignKey(related_name='secondary_contact_set', verbose_name=b'Secondary Brotherhood Contact', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('organization', models.ForeignKey(default=0, to='organization.Organization')),
                ('picture', models.ImageField(null=True, upload_to=b'profile_picture', blank=True)),
                ('rush_period', models.ManyToManyField(to=b'rushperiod.RushPeriod')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
