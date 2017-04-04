# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='finish',
            field=models.DateTimeField(null=True, verbose_name=b'date ended'),
        ),
        migrations.AlterField(
            model_name='process',
            name='start',
            field=models.DateTimeField(null=True, verbose_name=b'date started'),
        ),
    ]
