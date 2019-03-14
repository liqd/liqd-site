# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.images.blocks
import wagtail.core.fields
import wagtail.core.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160401_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body_de',
            field=wagtail.core.fields.StreamField((('standard_paragraph', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True))))), ('highlight_paragraph', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))))), ('quote_paragraph', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.RichTextBlock(required=True)), ('color', wagtail.core.blocks.ChoiceBlock(help_text='Select a color from the list.', choices=[('green', 'Gruen'), ('orange', 'Orange'), ('red', 'Rot')], required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), ('author', wagtail.core.blocks.CharBlock(length=256, required=False))))), ('single_image', wagtail.images.blocks.ImageChooserBlock(template='blocks/block_image.html', label='Single image', icon='image')), ('image_slider', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(), template='blocks/block_carousel.html', help_text='Responsive image slider (swipe on mobile). Please choose 4 images.', label='Image Slider', icon='image')), ('columns', wagtail.core.blocks.StructBlock((('col1_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col1_text', wagtail.core.blocks.RichTextBlock(required=True)), ('col2_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col2_text', wagtail.core.blocks.RichTextBlock(required=True))))), ('linkbox', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(length=256))))))))), ('project_teaser', wagtail.core.blocks.StructBlock((('translated_title', wagtail.core.blocks.CharBlock(length=256, required=False)), ('translated_shorttext', wagtail.core.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False))))), ('ThreeImageLinks', wagtail.core.blocks.StructBlock((('image_left', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True, label='Image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)), ('image_middle', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True, label='Image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)), ('image_right', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True, label='Image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)))))), null=True, verbose_name='Body', blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.core.fields.StreamField((('standard_paragraph', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True))))), ('highlight_paragraph', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))))), ('quote_paragraph', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.RichTextBlock(required=True)), ('color', wagtail.core.blocks.ChoiceBlock(help_text='Select a color from the list.', choices=[('green', 'Gruen'), ('orange', 'Orange'), ('red', 'Rot')], required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), ('author', wagtail.core.blocks.CharBlock(length=256, required=False))))), ('single_image', wagtail.images.blocks.ImageChooserBlock(template='blocks/block_image.html', label='Single image', icon='image')), ('image_slider', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(), template='blocks/block_carousel.html', help_text='Responsive image slider (swipe on mobile). Please choose 4 images.', label='Image Slider', icon='image')), ('columns', wagtail.core.blocks.StructBlock((('col1_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col1_text', wagtail.core.blocks.RichTextBlock(required=True)), ('col2_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col2_text', wagtail.core.blocks.RichTextBlock(required=True))))), ('linkbox', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(length=256))))))))), ('project_teaser', wagtail.core.blocks.StructBlock((('translated_title', wagtail.core.blocks.CharBlock(length=256, required=False)), ('translated_shorttext', wagtail.core.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False))))), ('ThreeImageLinks', wagtail.core.blocks.StructBlock((('image_left', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True, label='Image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)), ('image_middle', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True, label='Image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)), ('image_right', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True, label='Image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)))))), null=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='heading1_de',
            field=models.CharField(default='', verbose_name='Title top', blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='heading1_en',
            field=models.CharField(default='', verbose_name='Title top', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='heading2_de',
            field=models.CharField(default='', verbose_name='Title bottom', blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='heading2_en',
            field=models.CharField(default='', verbose_name='Title bottom', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='intro_de',
            field=wagtail.core.fields.RichTextField(verbose_name='Teasertext', blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='intro_en',
            field=wagtail.core.fields.RichTextField(verbose_name='Teasertext', blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='title_de',
            field=models.CharField(verbose_name='Title', blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='title_en',
            field=models.CharField(verbose_name='Title', max_length=255),
        ),
        migrations.AlterField(
            model_name='joinuspage',
            name='body_de',
            field=wagtail.core.fields.StreamField((('standard_paragraph', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True))))), ('highlight_paragraph', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))))), ('quote_paragraph', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.RichTextBlock(required=True)), ('color', wagtail.core.blocks.ChoiceBlock(help_text='Select a color from the list.', choices=[('green', 'Gruen'), ('orange', 'Orange'), ('red', 'Rot')], required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), ('author', wagtail.core.blocks.CharBlock(length=256, required=False))))), ('single_image', wagtail.images.blocks.ImageChooserBlock(template='blocks/block_image.html', label='Single image', icon='image')), ('image_slider', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(), template='blocks/block_carousel.html', help_text='Responsive image slider (swipe on mobile). Please choose 4 images.', label='Image Slider', icon='image')), ('columns', wagtail.core.blocks.StructBlock((('col1_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col1_text', wagtail.core.blocks.RichTextBlock(required=True)), ('col2_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col2_text', wagtail.core.blocks.RichTextBlock(required=True))))), ('linkbox', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(length=256))))))))), ('project_teaser', wagtail.core.blocks.StructBlock((('translated_title', wagtail.core.blocks.CharBlock(length=256, required=False)), ('translated_shorttext', wagtail.core.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False))))), ('ThreeImageLinks', wagtail.core.blocks.StructBlock((('image_left', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True, label='Image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)), ('image_middle', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True, label='Image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)), ('image_right', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True, label='Image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)))))), null=True, verbose_name='Body', blank=True),
        ),
        migrations.AlterField(
            model_name='joinuspage',
            name='body_en',
            field=wagtail.core.fields.StreamField((('standard_paragraph', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True))))), ('highlight_paragraph', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))))), ('quote_paragraph', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.RichTextBlock(required=True)), ('color', wagtail.core.blocks.ChoiceBlock(help_text='Select a color from the list.', choices=[('green', 'Gruen'), ('orange', 'Orange'), ('red', 'Rot')], required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), ('author', wagtail.core.blocks.CharBlock(length=256, required=False))))), ('single_image', wagtail.images.blocks.ImageChooserBlock(template='blocks/block_image.html', label='Single image', icon='image')), ('image_slider', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(), template='blocks/block_carousel.html', help_text='Responsive image slider (swipe on mobile). Please choose 4 images.', label='Image Slider', icon='image')), ('columns', wagtail.core.blocks.StructBlock((('col1_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col1_text', wagtail.core.blocks.RichTextBlock(required=True)), ('col2_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col2_text', wagtail.core.blocks.RichTextBlock(required=True))))), ('linkbox', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(length=256))))))))), ('project_teaser', wagtail.core.blocks.StructBlock((('translated_title', wagtail.core.blocks.CharBlock(length=256, required=False)), ('translated_shorttext', wagtail.core.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False))))), ('ThreeImageLinks', wagtail.core.blocks.StructBlock((('image_left', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True, label='Image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)), ('image_middle', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True, label='Image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)), ('image_right', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True, label='Image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)))))), null=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='joinuspage',
            name='intro_de',
            field=wagtail.core.fields.RichTextField(verbose_name='Teasertext', blank=True),
        ),
        migrations.AlterField(
            model_name='joinuspage',
            name='intro_en',
            field=wagtail.core.fields.RichTextField(verbose_name='Teasertext', blank=True),
        ),
        migrations.AlterField(
            model_name='joinuspage',
            name='title_de',
            field=models.CharField(verbose_name='Title', blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='joinuspage',
            name='title_en',
            field=models.CharField(verbose_name='Title', max_length=255),
        ),
        migrations.AlterField(
            model_name='liqdsettings',
            name='liqd_preliminary_site',
            field=models.BooleanField(default=False, help_text='Phase One of the new site, this setting can be deleted when the full site is ready to go live'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menu_title_de',
            field=models.CharField(verbose_name='Menu Title de', max_length=255),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menu_title_en',
            field=models.CharField(verbose_name='Menu Title en', blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='presslink',
            name='date',
            field=models.DateField(verbose_name='Post date'),
        ),
        migrations.AlterField(
            model_name='textpage',
            name='title_de',
            field=models.CharField(verbose_name='Header Title', blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='textpage',
            name='title_en',
            field=models.CharField(verbose_name='Header Title', blank=True, max_length=255),
        ),
    ]
