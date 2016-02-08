# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_auto_20160203_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='founded',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='metric',
            name='end_date',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='metric',
            name='start_date',
            field=models.CharField(max_length=12),
        ),
    ]
