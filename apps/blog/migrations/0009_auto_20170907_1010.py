# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-07 08:10
from __future__ import unicode_literals

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations

import apps.core.blocks
import apps.persons.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_merge_20170630_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexpage',
            name='body_de',
            field=wagtail.fields.StreamField((('standard_paragraph', wagtail.blocks.StructBlock((('headline', wagtail.blocks.CharBlock(length=256, required=False)), ('text', wagtail.blocks.RichTextBlock(required=True))))), ('highlight_paragraph', wagtail.blocks.StructBlock((('headline', wagtail.blocks.CharBlock(length=256, required=False)), ('text', wagtail.blocks.RichTextBlock(required=True)), ('link', wagtail.blocks.PageChooserBlock(required=False))))), ('quote_paragraph', wagtail.blocks.StructBlock((('text', wagtail.blocks.RichTextBlock(required=True)), ('color', wagtail.blocks.ChoiceBlock(choices=[('green', 'Gruen'), ('orange', 'Orange'), ('red', 'Rot')], help_text='Select a color from the list.', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), ('author', wagtail.blocks.CharBlock(length=256, required=False))))), ('single_image', wagtail.images.blocks.ImageChooserBlock(icon='image', label='Single image', template='blocks/block_image.html')), ('image_slider', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(), help_text='Responsive image slider (swipe on mobile). Please choose 4 images.', icon='image', label='Image Slider', template='blocks/block_carousel.html')), ('aligned_image', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('display', wagtail.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='Decide on which side the image should be displayed'))))), ('columns', wagtail.blocks.StructBlock((('col1_headline', wagtail.blocks.CharBlock(length=256, required=False)), ('col1_text', wagtail.blocks.RichTextBlock(required=True)), ('col1_url', wagtail.blocks.URLBlock(required=False)), ('col2_headline', wagtail.blocks.CharBlock(length=256, required=False)), ('col2_text', wagtail.blocks.RichTextBlock(required=True)), ('col2_url', wagtail.blocks.URLBlock(required=False))))), ('linkbox', wagtail.blocks.StructBlock((('headline', wagtail.blocks.CharBlock(length=256, required=False)), ('text', wagtail.blocks.RichTextBlock(required=False)), ('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(length=256))))))))), ('projects', wagtail.blocks.StructBlock((('headline', wagtail.blocks.CharBlock(length=256, required=False)), ('projects', wagtail.blocks.ListBlock(apps.core.blocks.ProjectBlock))))), ('ThreeImageLinks', wagtail.blocks.StructBlock((('image_left', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.blocks.CharBlock(length=256))), required=True)), ('image_middle', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.blocks.CharBlock(length=256))), required=True)), ('image_right', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.blocks.CharBlock(length=256))), required=True))))), ('Raw_HTML', wagtail.blocks.StructBlock((('headline', wagtail.blocks.CharBlock(length=256, required=False)), ('body', wagtail.blocks.RawHTMLBlock())))), ('Person', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('personlist', wagtail.blocks.ListBlock(apps.persons.models.PersonDisplayBlock))))), ('all_persons_list', wagtail.blocks.StructBlock((('headline', wagtail.blocks.CharBlock(required=False)),))), ('teaser_list', wagtail.blocks.StructBlock((('headline', wagtail.blocks.CharBlock(length=256, required=False)), ('teasers', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('headline', wagtail.blocks.CharBlock(length=256, required=False)), ('text', wagtail.blocks.RichTextBlock(required=True)), ('url', wagtail.blocks.URLBlock(required=False)))))))))), blank=True, null=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='blogindexpage',
            name='body_en',
            field=wagtail.fields.StreamField((('standard_paragraph', wagtail.blocks.StructBlock((('headline', wagtail.blocks.CharBlock(length=256, required=False)), ('text', wagtail.blocks.RichTextBlock(required=True))))), ('highlight_paragraph', wagtail.blocks.StructBlock((('headline', wagtail.blocks.CharBlock(length=256, required=False)), ('text', wagtail.blocks.RichTextBlock(required=True)), ('link', wagtail.blocks.PageChooserBlock(required=False))))), ('quote_paragraph', wagtail.blocks.StructBlock((('text', wagtail.blocks.RichTextBlock(required=True)), ('color', wagtail.blocks.ChoiceBlock(choices=[('green', 'Gruen'), ('orange', 'Orange'), ('red', 'Rot')], help_text='Select a color from the list.', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), ('author', wagtail.blocks.CharBlock(length=256, required=False))))), ('single_image', wagtail.images.blocks.ImageChooserBlock(icon='image', label='Single image', template='blocks/block_image.html')), ('image_slider', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(), help_text='Responsive image slider (swipe on mobile). Please choose 4 images.', icon='image', label='Image Slider', template='blocks/block_carousel.html')), ('aligned_image', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('display', wagtail.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='Decide on which side the image should be displayed'))))), ('columns', wagtail.blocks.StructBlock((('col1_headline', wagtail.blocks.CharBlock(length=256, required=False)), ('col1_text', wagtail.blocks.RichTextBlock(required=True)), ('col1_url', wagtail.blocks.URLBlock(required=False)), ('col2_headline', wagtail.blocks.CharBlock(length=256, required=False)), ('col2_text', wagtail.blocks.RichTextBlock(required=True)), ('col2_url', wagtail.blocks.URLBlock(required=False))))), ('linkbox', wagtail.blocks.StructBlock((('headline', wagtail.blocks.CharBlock(length=256, required=False)), ('text', wagtail.blocks.RichTextBlock(required=False)), ('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(length=256))))))))), ('projects', wagtail.blocks.StructBlock((('headline', wagtail.blocks.CharBlock(length=256, required=False)), ('projects', wagtail.blocks.ListBlock(apps.core.blocks.ProjectBlock))))), ('ThreeImageLinks', wagtail.blocks.StructBlock((('image_left', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.blocks.CharBlock(length=256))), required=True)), ('image_middle', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.blocks.CharBlock(length=256))), required=True)), ('image_right', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.blocks.CharBlock(length=256))), required=True))))), ('Raw_HTML', wagtail.blocks.StructBlock((('headline', wagtail.blocks.CharBlock(length=256, required=False)), ('body', wagtail.blocks.RawHTMLBlock())))), ('Person', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('personlist', wagtail.blocks.ListBlock(apps.persons.models.PersonDisplayBlock))))), ('all_persons_list', wagtail.blocks.StructBlock((('headline', wagtail.blocks.CharBlock(required=False)),))), ('teaser_list', wagtail.blocks.StructBlock((('headline', wagtail.blocks.CharBlock(length=256, required=False)), ('teasers', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('headline', wagtail.blocks.CharBlock(length=256, required=False)), ('text', wagtail.blocks.RichTextBlock(required=True)), ('url', wagtail.blocks.URLBlock(required=False)))))))))), null=True, verbose_name='Body'),
        ),
    ]
