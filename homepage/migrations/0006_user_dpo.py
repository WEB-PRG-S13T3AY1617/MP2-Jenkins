# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_remove_post_itemtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dpo',
            field=models.CharField(default='default', max_length=20),
        ),
    ]
