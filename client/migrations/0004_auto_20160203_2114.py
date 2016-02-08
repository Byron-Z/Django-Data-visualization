# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20160203_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.CharField(max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='founded',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='series',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='valuation',
            field=models.DecimalField(null=True, max_digits=32, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='metric',
            name='company',
            field=models.ForeignKey(to='client.Company', db_column=b'company_name'),
        ),
    ]
