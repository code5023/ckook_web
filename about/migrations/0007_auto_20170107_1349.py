# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_auto_20170107_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='strapline',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
