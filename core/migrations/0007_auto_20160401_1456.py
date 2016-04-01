# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20160401_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='heading1_de',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='heading1_en',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='heading2_de',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='heading2_en',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='title_en',
            field=models.CharField(max_length=255, verbose_name=b'Header Title'),
        ),
        migrations.AlterField(
            model_name='joinuspage',
            name='title_en',
            field=models.CharField(max_length=255, verbose_name=b'Header Title'),
        ),
    ]
