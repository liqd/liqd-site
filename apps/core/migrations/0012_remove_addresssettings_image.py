# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-19 12:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_addresssettings_custom_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addresssettings',
            name='image',
        ),
    ]
