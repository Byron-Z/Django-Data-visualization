# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_auto_20160203_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metric',
            name='company',
            field=models.ForeignKey(to='client.Company', db_column=b'company_name', to_field=b'name'),
        ),
    ]
