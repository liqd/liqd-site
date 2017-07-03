# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-28 08:44
from __future__ import unicode_literals

import apps.core.blocks
import apps.persons.models
from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_add_statistics_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectindexpage',
            name='body_de',
            field=wagtail.wagtailcore.fields.StreamField((('standard_paragraph', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), ('text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))))), ('highlight_paragraph', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), ('text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))))), ('quote_paragraph', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), ('color', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('green', 'Gruen'), ('orange', 'Orange'), ('red', 'Rot')], help_text='Select a color from the list.', required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text='Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), ('author', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False))))), ('single_image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image', label='Single image', template='blocks/block_image.html')), ('image_slider', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailimages.blocks.ImageChooserBlock(), help_text='Responsive image slider (swipe on mobile). Please choose 4 images.', icon='image', label='Image Slider', template='blocks/block_carousel.html')), ('columns', wagtail.wagtailcore.blocks.StructBlock((('col1_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), ('col1_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), ('col1_url', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('col2_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), ('col2_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), ('col2_url', wagtail.wagtailcore.blocks.URLBlock(required=False))))), ('linkbox', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), ('text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock()), ('link_text', wagtail.wagtailcore.blocks.CharBlock(length=256))))))))), ('projects', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), ('projects', wagtail.wagtailcore.blocks.ListBlock(apps.core.blocks.ProjectBlock))))), ('ThreeImageLinks', wagtail.wagtailcore.blocks.StructBlock((('image_left', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.wagtailcore.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(length=256))), required=True)), ('image_middle', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.wagtailcore.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(length=256))), required=True)), ('image_right', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.wagtailcore.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(length=256))), required=True))))), ('Raw_HTML', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), ('body', wagtail.wagtailcore.blocks.RawHTMLBlock())))), ('Person', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title', required=False)), ('personlist', wagtail.wagtailcore.blocks.ListBlock(apps.persons.models.PersonDisplayBlock)))))), blank=True, null=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='projectindexpage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField((('standard_paragraph', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), ('text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))))), ('highlight_paragraph', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), ('text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), ('link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))))), ('quote_paragraph', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), ('color', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('green', 'Gruen'), ('orange', 'Orange'), ('red', 'Rot')], help_text='Select a color from the list.', required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text='Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), ('author', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False))))), ('single_image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image', label='Single image', template='blocks/block_image.html')), ('image_slider', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailimages.blocks.ImageChooserBlock(), help_text='Responsive image slider (swipe on mobile). Please choose 4 images.', icon='image', label='Image Slider', template='blocks/block_carousel.html')), ('columns', wagtail.wagtailcore.blocks.StructBlock((('col1_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), ('col1_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), ('col1_url', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('col2_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), ('col2_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), ('col2_url', wagtail.wagtailcore.blocks.URLBlock(required=False))))), ('linkbox', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), ('text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock()), ('link_text', wagtail.wagtailcore.blocks.CharBlock(length=256))))))))), ('projects', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), ('projects', wagtail.wagtailcore.blocks.ListBlock(apps.core.blocks.ProjectBlock))))), ('ThreeImageLinks', wagtail.wagtailcore.blocks.StructBlock((('image_left', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.wagtailcore.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(length=256))), required=True)), ('image_middle', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.wagtailcore.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(length=256))), required=True)), ('image_right', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.wagtailcore.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(length=256))), required=True))))), ('Raw_HTML', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), ('body', wagtail.wagtailcore.blocks.RawHTMLBlock())))), ('Person', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title', required=False)), ('personlist', wagtail.wagtailcore.blocks.ListBlock(apps.persons.models.PersonDisplayBlock)))))), null=True, verbose_name='Body'),
        ),
    ]
