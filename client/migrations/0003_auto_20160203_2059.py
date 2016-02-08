# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20160203_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.CharField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='company',
            name='founded',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='metric',
            name='end_date',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='metric',
            name='start_date',
            field=models.CharField(max_length=16),
        ),
    ]
