# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_liqdsettings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='body_de',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='body_en',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='heading_de',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='heading_en',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='intro_de',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='intro_en',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='search_description_de',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='search_description_en',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='seo_title_de',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='seo_title_en',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='slug_de',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='slug_en',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='title_de',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='url_path_de',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='url_path_en',
        ),
    ]
