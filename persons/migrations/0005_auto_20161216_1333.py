# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0029_unicode_slugfield_dj19'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('persons', '0004_personsnippet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personindexpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='personpage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='personpage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='personpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='PersonIndexPage',
        ),
        migrations.DeleteModel(
            name='PersonPage',
        ),
    ]
