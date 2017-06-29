# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-21 13:24
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove-person-bg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body_de',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('aligned_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Image')), ('display', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='Decide on which side the image should be displayed'))), icon='image')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), ('Raw_HTML', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), ('body', wagtail.wagtailcore.blocks.RawHTMLBlock()))))), blank=True, null=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('aligned_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(label='Image')), ('display', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='Decide on which side the image should be displayed'))), icon='image')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), ('Raw_HTML', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), ('body', wagtail.wagtailcore.blocks.RawHTMLBlock()))))), null=True, verbose_name='Body'),
        ),
    ]
