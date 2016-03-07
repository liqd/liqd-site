# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20160224_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectindexpage',
            name='intro_de',
        ),
        migrations.RemoveField(
            model_name='projectindexpage',
            name='intro_en',
        ),
        migrations.RemoveField(
            model_name='projectindexpage',
            name='search_description_de',
        ),
        migrations.RemoveField(
            model_name='projectindexpage',
            name='search_description_en',
        ),
        migrations.RemoveField(
            model_name='projectindexpage',
            name='seo_title_de',
        ),
        migrations.RemoveField(
            model_name='projectindexpage',
            name='seo_title_en',
        ),
        migrations.RemoveField(
            model_name='projectindexpage',
            name='slug_de',
        ),
        migrations.RemoveField(
            model_name='projectindexpage',
            name='slug_en',
        ),
        migrations.RemoveField(
            model_name='projectindexpage',
            name='title_de',
        ),
        migrations.RemoveField(
            model_name='projectindexpage',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='projectindexpage',
            name='url_path_de',
        ),
        migrations.RemoveField(
            model_name='projectindexpage',
            name='url_path_en',
        ),
    ]
