# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-06 06:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('closedverse_main', '0012_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_source', to=settings.AUTH_USER_MODEL)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_target', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]