# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160329_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='body',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='blogpage',
            name='subtitle_de',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='subtitle_en',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
    ]
