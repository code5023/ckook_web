# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_auto_20170107_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]