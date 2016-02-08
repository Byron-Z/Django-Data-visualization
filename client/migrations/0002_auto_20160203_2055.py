# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='founding_date',
            new_name='founded',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='company_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='post_money_valuation',
            new_name='valuation',
        ),
        migrations.RenameField(
            model_name='metric',
            old_name='company_name',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='metric',
            old_name='metric_name',
            new_name='name',
        ),
    ]
