# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-06 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0003_auto_20180806_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name='手机号'),
        ),
    ]
