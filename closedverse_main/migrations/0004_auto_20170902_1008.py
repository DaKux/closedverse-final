# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-02 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closedverse_main', '0003_auto_20170902_0234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentarchive',
            name='comment_ptr',
        ),
        migrations.RemoveField(
            model_name='postarchive',
            name='post_ptr',
        ),
        migrations.AddField(
            model_name='comment',
            name='is_rm',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='is_rm',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='CommentArchive',
        ),
        migrations.DeleteModel(
            name='PostArchive',
        ),
    ]