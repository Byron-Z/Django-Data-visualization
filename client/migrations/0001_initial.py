# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(unique=True, max_length=128)),
                ('founding_date', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=1024)),
                ('series', models.CharField(max_length=32)),
                ('post_money_valuation', models.DecimalField(max_digits=32, decimal_places=5)),
            ],
            options={
                'db_table': 'company',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('metric_name', models.CharField(unique=True, max_length=128)),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
                ('value', models.IntegerField()),
                ('company_name', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'metric',
            },
            bases=(models.Model,),
        ),
    ]
