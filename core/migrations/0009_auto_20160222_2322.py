# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail_modeltranslation.models
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('core', '0008_auto_20150716_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('title_de', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_en', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('slug_de', models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_en', models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('url_path_de', models.TextField(verbose_name='URL path', null=True, editable=False, blank=True)),
                ('url_path_en', models.TextField(verbose_name='URL path', null=True, editable=False, blank=True)),
                ('seo_title_de', models.CharField(help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title', blank=True)),
                ('seo_title_en', models.CharField(help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title', blank=True)),
                ('search_description_de', models.TextField(null=True, verbose_name='search description', blank=True)),
                ('search_description_en', models.TextField(null=True, verbose_name='search description', blank=True)),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('body_de', wagtail.wagtailcore.fields.RichTextField(null=True, blank=True)),
                ('body_en', wagtail.wagtailcore.fields.RichTextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail_modeltranslation.models.TranslationMixin, 'wagtailcore.page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_de',
            field=wagtail.wagtailcore.fields.StreamField([(b'heading', wagtail.wagtailcore.blocks.CharBlock(classname=b'full title', icon=b'title')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'pilcrow')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image'))], null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField([(b'heading', wagtail.wagtailcore.blocks.CharBlock(classname=b'full title', icon=b'title')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'pilcrow')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image'))], null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='heading',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='heading_de',
            field=models.CharField(default=b'', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='heading_en',
            field=models.CharField(default=b'', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro_de',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro_en',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='search_description_de',
            field=models.TextField(null=True, verbose_name='search description', blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='search_description_en',
            field=models.TextField(null=True, verbose_name='search description', blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='seo_title_de',
            field=models.CharField(help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title', blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='seo_title_en',
            field=models.CharField(help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title', blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='slug_de',
            field=models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='slug_en',
            field=models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_de',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='url_path_de',
            field=models.TextField(verbose_name='URL path', null=True, editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='url_path_en',
            field=models.TextField(verbose_name='URL path', null=True, editable=False, blank=True),
        ),
    ]
