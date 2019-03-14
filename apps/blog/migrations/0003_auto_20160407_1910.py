# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.images.blocks
import wagtail.core.fields
import wagtail.core.blocks
import wagtail.embeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160401_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexpage',
            name='body_de',
            field=wagtail.core.fields.StreamField((('standard_paragraph', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True))))), ('highlight_paragraph', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))))), ('quote_paragraph', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.RichTextBlock(required=True)), ('color', wagtail.core.blocks.ChoiceBlock(help_text='Select a color from the list.', choices=[('green', 'Gruen'), ('orange', 'Orange'), ('red', 'Rot')], required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), ('author', wagtail.core.blocks.CharBlock(length=256, required=False))))), ('single_image', wagtail.images.blocks.ImageChooserBlock(template='blocks/block_image.html', label='Single image', icon='image')), ('image_slider', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(), template='blocks/block_carousel.html', help_text='Responsive image slider (swipe on mobile). Please choose 4 images.', label='Image Slider', icon='image')), ('columns', wagtail.core.blocks.StructBlock((('col1_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col1_text', wagtail.core.blocks.RichTextBlock(required=True)), ('col2_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col2_text', wagtail.core.blocks.RichTextBlock(required=True))))), ('linkbox', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(length=256))))))))), ('project_teaser', wagtail.core.blocks.StructBlock((('translated_title', wagtail.core.blocks.CharBlock(length=256, required=False)), ('translated_shorttext', wagtail.core.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False))))), ('ThreeImageLinks', wagtail.core.blocks.StructBlock((('image_left', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True, label='Image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)), ('image_middle', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True, label='Image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)), ('image_right', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True, label='Image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)))))), null=True, verbose_name='Body', blank=True),
        ),
        migrations.AlterField(
            model_name='blogindexpage',
            name='body_en',
            field=wagtail.core.fields.StreamField((('standard_paragraph', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True))))), ('highlight_paragraph', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))))), ('quote_paragraph', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.RichTextBlock(required=True)), ('color', wagtail.core.blocks.ChoiceBlock(help_text='Select a color from the list.', choices=[('green', 'Gruen'), ('orange', 'Orange'), ('red', 'Rot')], required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), ('author', wagtail.core.blocks.CharBlock(length=256, required=False))))), ('single_image', wagtail.images.blocks.ImageChooserBlock(template='blocks/block_image.html', label='Single image', icon='image')), ('image_slider', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(), template='blocks/block_carousel.html', help_text='Responsive image slider (swipe on mobile). Please choose 4 images.', label='Image Slider', icon='image')), ('columns', wagtail.core.blocks.StructBlock((('col1_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col1_text', wagtail.core.blocks.RichTextBlock(required=True)), ('col2_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('col2_text', wagtail.core.blocks.RichTextBlock(required=True))))), ('linkbox', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(length=256))))))))), ('project_teaser', wagtail.core.blocks.StructBlock((('translated_title', wagtail.core.blocks.CharBlock(length=256, required=False)), ('translated_shorttext', wagtail.core.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False))))), ('ThreeImageLinks', wagtail.core.blocks.StructBlock((('image_left', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True, label='Image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)), ('image_middle', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True, label='Image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)), ('image_right', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True, label='Image')), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), ('link_text', wagtail.core.blocks.CharBlock(length=256))), required=True)))))), null=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='blogindexpage',
            name='intro_de',
            field=wagtail.core.fields.RichTextField(verbose_name='Teasertext', blank=True),
        ),
        migrations.AlterField(
            model_name='blogindexpage',
            name='intro_en',
            field=wagtail.core.fields.RichTextField(verbose_name='Teasertext', blank=True),
        ),
        migrations.AlterField(
            model_name='blogindexpage',
            name='title_de',
            field=models.CharField(verbose_name='Title', blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='blogindexpage',
            name='title_en',
            field=models.CharField(verbose_name='Title', max_length=255),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body_de',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('video', wagtail.embeds.blocks.EmbedBlock(icon='media'))), null=True, verbose_name='Body', blank=True),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body_en',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('video', wagtail.embeds.blocks.EmbedBlock(icon='media'))), null=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(verbose_name='Post date'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='intro_de',
            field=wagtail.core.fields.RichTextField(verbose_name='Teasertext', blank=True),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='intro_en',
            field=wagtail.core.fields.RichTextField(verbose_name='Teasertext'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='subtitle_de',
            field=models.CharField(default='', verbose_name='Subtitle', blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='subtitle_en',
            field=models.CharField(default='', verbose_name='Subtitle', max_length=255),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='title_de',
            field=models.CharField(verbose_name='Title', blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='title_en',
            field=models.CharField(verbose_name='Title', max_length=255),
        ),
    ]
