# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-04 09:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgpi', '0003_auto_20180904_0939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='greet',
            old_name='greets',
            new_name='greetings',
        ),
    ]
