# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-20 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Greet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gret', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Resp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rsp', models.CharField(max_length=100)),
            ],
        ),
    ]