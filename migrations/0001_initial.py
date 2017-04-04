# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pid', models.IntegerField(default=0)),
                ('pname', models.CharField(max_length=200)),
                ('start', models.DateTimeField(verbose_name=b'date started')),
                ('finish', models.DateTimeField(verbose_name=b'date ended')),
                ('status', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProcUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.IntegerField(default=0)),
                ('pid', models.ForeignKey(to='traffic.Process')),
            ],
        ),
    ]
