# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-31 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closedverse_main', '0005_auto_20170731_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=32, null=True),
        ),
    ]