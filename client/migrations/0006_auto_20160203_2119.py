# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_auto_20160203_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='founded',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='metric',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='metric',
            name='start_date',
            field=models.DateField(),
        ),
    ]
