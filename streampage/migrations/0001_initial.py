# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail_modeltranslation.models
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinUsPage',
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
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('intro_de', wagtail.wagtailcore.fields.RichTextField(null=True, blank=True)),
                ('intro_en', wagtail.wagtailcore.fields.RichTextField(null=True, blank=True)),
                ('body', wagtail.wagtailcore.fields.StreamField([(b'standard_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))], template=b'blocks/block_standard_paragraph.html')), (b'highlight_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))], template=b'blocks/block_highlight_paragraph.html')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'columns', wagtail.wagtailcore.blocks.StructBlock([(b'col1_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=True)), (b'col1_text', wagtail.wagtailcore.blocks.RichTextBlock()), (b'col2_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=True)), (b'col2_text', wagtail.wagtailcore.blocks.RichTextBlock())], template=b'blocks/block_column.html')), (b'carousel', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailimages.blocks.ImageChooserBlock(), help_text=b'Please choose up to 4 images.', template=b'blocks/block_carousel.html')), (b'linkbox', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.PageChooserBlock(), template=b'blocks/block_internalLink.html'))], template=b'blocks/block_linkbox.html'))])),
                ('body_de', wagtail.wagtailcore.fields.StreamField([(b'standard_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))], template=b'blocks/block_standard_paragraph.html')), (b'highlight_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))], template=b'blocks/block_highlight_paragraph.html')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'columns', wagtail.wagtailcore.blocks.StructBlock([(b'col1_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=True)), (b'col1_text', wagtail.wagtailcore.blocks.RichTextBlock()), (b'col2_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=True)), (b'col2_text', wagtail.wagtailcore.blocks.RichTextBlock())], template=b'blocks/block_column.html')), (b'carousel', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailimages.blocks.ImageChooserBlock(), help_text=b'Please choose up to 4 images.', template=b'blocks/block_carousel.html')), (b'linkbox', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.PageChooserBlock(), template=b'blocks/block_internalLink.html'))], template=b'blocks/block_linkbox.html'))], null=True)),
                ('body_en', wagtail.wagtailcore.fields.StreamField([(b'standard_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))], template=b'blocks/block_standard_paragraph.html')), (b'highlight_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))], template=b'blocks/block_highlight_paragraph.html')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'columns', wagtail.wagtailcore.blocks.StructBlock([(b'col1_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=True)), (b'col1_text', wagtail.wagtailcore.blocks.RichTextBlock()), (b'col2_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=True)), (b'col2_text', wagtail.wagtailcore.blocks.RichTextBlock())], template=b'blocks/block_column.html')), (b'carousel', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailimages.blocks.ImageChooserBlock(), help_text=b'Please choose up to 4 images.', template=b'blocks/block_carousel.html')), (b'linkbox', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.PageChooserBlock(), template=b'blocks/block_internalLink.html'))], template=b'blocks/block_linkbox.html'))], null=True)),
            ],
            options={
                'verbose_name': 'JoinUs Page',
            },
            bases=(wagtail_modeltranslation.models.TranslationMixin, 'wagtailcore.page'),
        ),
    ]
