# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20160401_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexpage',
            name='title_en',
            field=models.CharField(max_length=255, verbose_name=b'Header Title'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='intro_en',
            field=wagtail.wagtailcore.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='subtitle_en',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='title_en',
            field=models.CharField(max_length=255, verbose_name=b'Header Title'),
        ),
    ]
