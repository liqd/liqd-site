# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-08 10:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170607_1421'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='joinuspage',
            options={'verbose_name': 'Default Page with several Blocks'},
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='heading1_de',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='heading1_en',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='heading2_de',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='heading2_en',
        ),
    ]
