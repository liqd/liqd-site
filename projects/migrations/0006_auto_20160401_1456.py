# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20160401_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectindexpage',
            name='title_en',
            field=models.CharField(max_length=255, verbose_name=b'Header Title'),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='title_en',
            field=models.CharField(max_length=255, verbose_name=b'Header Title'),
        ),
    ]
