# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_user_dpo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='itemtype',
            field=models.CharField(default='default', max_length=10),
        ),
    ]