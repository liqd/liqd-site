# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160329_1653'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogindexpage',
            options={'managed': True, 'verbose_name': 'Extended Page'},
        ),
        migrations.RemoveField(
            model_name='blogindexpage',
            name='intro',
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='body_de',
            field=wagtail.wagtailcore.fields.StreamField([(b'standard_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))])), (b'highlight_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))])), (b'quote_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'color', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Select a color from the list.', required=False, choices=[(b'green', b'Gruen'), (b'orange', b'Orange'), (b'red', b'Rot')])), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text=b'Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), (b'author', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False))])), (b'single_image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image', template=b'blocks/block_image.html', label=b'Single image')), (b'image_slider', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailimages.blocks.ImageChooserBlock(), help_text=b'Responsive image slider (swipe on mobile). Please choose 4 images.', icon=b'image', template=b'blocks/block_carousel.html', label=b'Image Slider')), (b'columns', wagtail.wagtailcore.blocks.StructBlock([(b'col1_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'col1_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'col2_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'col2_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))])), (b'linkbox', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock()), (b'link_text', wagtail.wagtailcore.blocks.CharBlock(length=256))])))])), (b'project_teaser', wagtail.wagtailcore.blocks.StructBlock([(b'translated_title', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'translated_shorttext', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'translated_image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'translated_external_url', wagtail.wagtailcore.blocks.URLBlock(length=256, required=False))]))], null=True, blank=True),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField([(b'standard_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))])), (b'highlight_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))])), (b'quote_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'color', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Select a color from the list.', required=False, choices=[(b'green', b'Gruen'), (b'orange', b'Orange'), (b'red', b'Rot')])), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text=b'Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), (b'author', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False))])), (b'single_image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image', template=b'blocks/block_image.html', label=b'Single image')), (b'image_slider', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailimages.blocks.ImageChooserBlock(), help_text=b'Responsive image slider (swipe on mobile). Please choose 4 images.', icon=b'image', template=b'blocks/block_carousel.html', label=b'Image Slider')), (b'columns', wagtail.wagtailcore.blocks.StructBlock([(b'col1_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'col1_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'col2_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'col2_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))])), (b'linkbox', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock()), (b'link_text', wagtail.wagtailcore.blocks.CharBlock(length=256))])))])), (b'project_teaser', wagtail.wagtailcore.blocks.StructBlock([(b'translated_title', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'translated_shorttext', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'translated_image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'translated_external_url', wagtail.wagtailcore.blocks.URLBlock(length=256, required=False))]))], null=True),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='intro_de',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='intro_en',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='title_de',
            field=models.CharField(max_length=255, verbose_name=b'Header Title', blank=True),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='title_en',
            field=models.CharField(max_length=255, verbose_name=b'Header Title', blank=True),
        ),
    ]
