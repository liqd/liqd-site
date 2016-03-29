# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpage_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpagetag',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='blogpagetag',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='blogparagraph',
            name='page',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='author_string',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='tags',
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='author',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='BlogPageTag',
        ),
        migrations.DeleteModel(
            name='BlogParagraph',
        ),
    ]
