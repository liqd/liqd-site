# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20160306_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textpage',
            name='search_description_de',
        ),
        migrations.RemoveField(
            model_name='textpage',
            name='search_description_en',
        ),
        migrations.RemoveField(
            model_name='textpage',
            name='seo_title_de',
        ),
        migrations.RemoveField(
            model_name='textpage',
            name='seo_title_en',
        ),
        migrations.RemoveField(
            model_name='textpage',
            name='slug_de',
        ),
        migrations.RemoveField(
            model_name='textpage',
            name='slug_en',
        ),
        migrations.RemoveField(
            model_name='textpage',
            name='title_de',
        ),
        migrations.RemoveField(
            model_name='textpage',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='textpage',
            name='url_path_de',
        ),
        migrations.RemoveField(
            model_name='textpage',
            name='url_path_en',
        ),
    ]
