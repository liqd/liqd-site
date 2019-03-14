# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-28 15:47
from __future__ import unicode_literals

import apps.core.blocks
import apps.persons.models
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20170628_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body_de',
            field=wagtail.core.fields.StreamField((('standard_paragraph', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True))))), ('highlight_paragraph', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))))), ('quote_paragraph', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.RichTextBlock(required=True)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('green', 'Gruen'), ('orange', 'Orange'), ('red', 'Rot')], help_text='Select a color from the list.', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), ('author', wagtail.core.blocks.CharBlock(length=256, required=False))))), ('single_image', wagtail.images.blocks.ImageChooserBlock(icon='image', label='Single image', template='blocks/block_image.html')), ('image_slider', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(), help_text='Responsive image slider (swipe on mobile). Please choose 4 images.', icon='image', label='Image Slider', template='blocks/block_carousel.html')), ('aligned_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('display', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='Decide on which side the image should be displayed'))))), ('columns', wagtail.core.blocks.StructBlock((('col1_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col1_text', wagtail.core.blocks.RichTextBlock(required=True)), ('col1_url', wagtail.core.blocks.URLBlock(required=False)), ('col2_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col2_text', wagtail.core.blocks.RichTextBlock(required=True)), ('col2_url', wagtail.core.blocks.URLBlock(required=False))))), ('linkbox', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(length=256))))))))), ('projects', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('projects', wagtail.core.blocks.ListBlock(apps.core.blocks.ProjectBlock))))), ('ThreeImageLinks', wagtail.core.blocks.StructBlock((('image_left', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)), ('image_middle', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)), ('image_right', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True))))), ('Raw_HTML', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('body', wagtail.core.blocks.RawHTMLBlock())))), ('Person', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title', required=False)), ('personlist', wagtail.core.blocks.ListBlock(apps.persons.models.PersonDisplayBlock))))), ('all_persons_list', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=False)),))), ('TeaserList', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('teasers', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True)), ('url', wagtail.core.blocks.URLBlock(required=False)))))))))), blank=True, null=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.core.fields.StreamField((('standard_paragraph', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True))))), ('highlight_paragraph', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))))), ('quote_paragraph', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.RichTextBlock(required=True)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('green', 'Gruen'), ('orange', 'Orange'), ('red', 'Rot')], help_text='Select a color from the list.', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), ('author', wagtail.core.blocks.CharBlock(length=256, required=False))))), ('single_image', wagtail.images.blocks.ImageChooserBlock(icon='image', label='Single image', template='blocks/block_image.html')), ('image_slider', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(), help_text='Responsive image slider (swipe on mobile). Please choose 4 images.', icon='image', label='Image Slider', template='blocks/block_carousel.html')), ('aligned_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('display', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='Decide on which side the image should be displayed'))))), ('columns', wagtail.core.blocks.StructBlock((('col1_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col1_text', wagtail.core.blocks.RichTextBlock(required=True)), ('col1_url', wagtail.core.blocks.URLBlock(required=False)), ('col2_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col2_text', wagtail.core.blocks.RichTextBlock(required=True)), ('col2_url', wagtail.core.blocks.URLBlock(required=False))))), ('linkbox', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(length=256))))))))), ('projects', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('projects', wagtail.core.blocks.ListBlock(apps.core.blocks.ProjectBlock))))), ('ThreeImageLinks', wagtail.core.blocks.StructBlock((('image_left', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)), ('image_middle', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)), ('image_right', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True))))), ('Raw_HTML', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('body', wagtail.core.blocks.RawHTMLBlock())))), ('Person', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title', required=False)), ('personlist', wagtail.core.blocks.ListBlock(apps.persons.models.PersonDisplayBlock))))), ('all_persons_list', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=False)),))), ('TeaserList', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('teasers', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True)), ('url', wagtail.core.blocks.URLBlock(required=False)))))))))), null=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='joinuspage',
            name='body_de',
            field=wagtail.core.fields.StreamField((('standard_paragraph', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True))))), ('highlight_paragraph', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))))), ('quote_paragraph', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.RichTextBlock(required=True)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('green', 'Gruen'), ('orange', 'Orange'), ('red', 'Rot')], help_text='Select a color from the list.', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), ('author', wagtail.core.blocks.CharBlock(length=256, required=False))))), ('single_image', wagtail.images.blocks.ImageChooserBlock(icon='image', label='Single image', template='blocks/block_image.html')), ('image_slider', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(), help_text='Responsive image slider (swipe on mobile). Please choose 4 images.', icon='image', label='Image Slider', template='blocks/block_carousel.html')), ('aligned_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('display', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='Decide on which side the image should be displayed'))))), ('columns', wagtail.core.blocks.StructBlock((('col1_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col1_text', wagtail.core.blocks.RichTextBlock(required=True)), ('col1_url', wagtail.core.blocks.URLBlock(required=False)), ('col2_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col2_text', wagtail.core.blocks.RichTextBlock(required=True)), ('col2_url', wagtail.core.blocks.URLBlock(required=False))))), ('linkbox', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(length=256))))))))), ('projects', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('projects', wagtail.core.blocks.ListBlock(apps.core.blocks.ProjectBlock))))), ('ThreeImageLinks', wagtail.core.blocks.StructBlock((('image_left', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)), ('image_middle', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)), ('image_right', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True))))), ('Raw_HTML', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('body', wagtail.core.blocks.RawHTMLBlock())))), ('Person', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title', required=False)), ('personlist', wagtail.core.blocks.ListBlock(apps.persons.models.PersonDisplayBlock))))), ('all_persons_list', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=False)),))), ('TeaserList', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('teasers', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True)), ('url', wagtail.core.blocks.URLBlock(required=False)))))))))), blank=True, null=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='joinuspage',
            name='body_en',
            field=wagtail.core.fields.StreamField((('standard_paragraph', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True))))), ('highlight_paragraph', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))))), ('quote_paragraph', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.RichTextBlock(required=True)), ('color', wagtail.core.blocks.ChoiceBlock(choices=[('green', 'Gruen'), ('orange', 'Orange'), ('red', 'Rot')], help_text='Select a color from the list.', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), ('author', wagtail.core.blocks.CharBlock(length=256, required=False))))), ('single_image', wagtail.images.blocks.ImageChooserBlock(icon='image', label='Single image', template='blocks/block_image.html')), ('image_slider', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(), help_text='Responsive image slider (swipe on mobile). Please choose 4 images.', icon='image', label='Image Slider', template='blocks/block_carousel.html')), ('aligned_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('display', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='Decide on which side the image should be displayed'))))), ('columns', wagtail.core.blocks.StructBlock((('col1_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col1_text', wagtail.core.blocks.RichTextBlock(required=True)), ('col1_url', wagtail.core.blocks.URLBlock(required=False)), ('col2_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col2_text', wagtail.core.blocks.RichTextBlock(required=True)), ('col2_url', wagtail.core.blocks.URLBlock(required=False))))), ('linkbox', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(length=256))))))))), ('projects', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('projects', wagtail.core.blocks.ListBlock(apps.core.blocks.ProjectBlock))))), ('ThreeImageLinks', wagtail.core.blocks.StructBlock((('image_left', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)), ('image_middle', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)), ('image_right', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=True)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True))))), ('Raw_HTML', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('body', wagtail.core.blocks.RawHTMLBlock())))), ('Person', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title', required=False)), ('personlist', wagtail.core.blocks.ListBlock(apps.persons.models.PersonDisplayBlock))))), ('all_persons_list', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(required=False)),))), ('TeaserList', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('teasers', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True)), ('url', wagtail.core.blocks.URLBlock(required=False)))))))))), null=True, verbose_name='Body'),
        ),
    ]
