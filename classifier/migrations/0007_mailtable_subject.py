# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-12 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0006_remove_mailtable_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailtable',
            name='subject',
            field=models.TextField(default='lol'),
            preserve_default=False,
        ),
    ]
