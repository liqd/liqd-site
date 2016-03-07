# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_projectpage_external_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectindexpage',
            name='intro_de',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='projectindexpage',
            name='intro_en',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='projectindexpage',
            name='search_description_de',
            field=models.TextField(null=True, verbose_name='search description', blank=True),
        ),
        migrations.AddField(
            model_name='projectindexpage',
            name='search_description_en',
            field=models.TextField(null=True, verbose_name='search description', blank=True),
        ),
        migrations.AddField(
            model_name='projectindexpage',
            name='seo_title_de',
            field=models.CharField(help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title', blank=True),
        ),
        migrations.AddField(
            model_name='projectindexpage',
            name='seo_title_en',
            field=models.CharField(help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title', blank=True),
        ),
        migrations.AddField(
            model_name='projectindexpage',
            name='slug_de',
            field=models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='projectindexpage',
            name='slug_en',
            field=models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='projectindexpage',
            name='title_de',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='projectindexpage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='projectindexpage',
            name='url_path_de',
            field=models.TextField(verbose_name='URL path', null=True, editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='projectindexpage',
            name='url_path_en',
            field=models.TextField(verbose_name='URL path', null=True, editable=False, blank=True),
        ),
    ]
