# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-13 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0010_auto_20160512_1737'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailtable',
            options={},
        ),
        migrations.AddField(
            model_name='mailtable',
            name='category',
            field=models.CharField(default='unclassified', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mailtable',
            name='classification',
            field=models.CharField(default='unclassified', max_length=100),
            preserve_default=False,
        ),
    ]
