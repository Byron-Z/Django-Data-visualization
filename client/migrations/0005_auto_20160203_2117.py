# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20160203_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='id',
        ),
        migrations.RemoveField(
            model_name='metric',
            name='id',
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=128, unique=True, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='metric',
            name='company',
            field=models.ForeignKey(to='client.Company'),
        ),
        migrations.AlterField(
            model_name='metric',
            name='name',
            field=models.CharField(max_length=128, unique=True, serialize=False, primary_key=True),
        ),
    ]
