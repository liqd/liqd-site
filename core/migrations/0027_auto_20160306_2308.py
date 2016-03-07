# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('core', '0026_joinuspage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='streamfieldpage',
            name='page_ptr',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='heading1',
            new_name='heading1_de',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='heading2',
            new_name='heading2_de',
        ),
        migrations.RenameField(
            model_name='joinuspage',
            old_name='body',
            new_name='body_de',
        ),
        migrations.RenameField(
            model_name='joinuspage',
            old_name='intro',
            new_name='intro_de',
        ),
        migrations.RenameField(
            model_name='textpage',
            old_name='body',
            new_name='body_de',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='body',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='intro',
        ),
        migrations.AddField(
            model_name='homepage',
            name='heading1_en',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='heading2_en',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='joinuspage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField([(b'standard_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))])), (b'highlight_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))])), (b'quote_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'color', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Select a color from the list.', required=False, choices=[(b'green', b'Gruen'), (b'orange', b'Orange'), (b'red', b'Rot')])), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text=b'Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), (b'author', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False))])), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image', label=b'Single image')), (b'columns', wagtail.wagtailcore.blocks.StructBlock([(b'col1_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'col1_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'col2_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'col2_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))])), (b'image_slider', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailimages.blocks.ImageChooserBlock(), help_text=b'Responsive image slider (swipe on mobile). Please choose 4 images.', icon=b'image', template=b'blocks/block_carousel.html', label=b'Image Slider')), (b'linkbox', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.PageChooserBlock()))])), (b'project_teaser', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'shorttext', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.wagtailcore.blocks.URLBlock(length=256, required=False))]))], null=True),
        ),
        migrations.AddField(
            model_name='joinuspage',
            name='intro_en',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='joinuspage',
            name='title_de',
            field=models.CharField(max_length=255, verbose_name=b'Header Title', blank=True),
        ),
        migrations.AddField(
            model_name='joinuspage',
            name='title_en',
            field=models.CharField(max_length=255, verbose_name=b'Header Title', blank=True),
        ),
        migrations.AddField(
            model_name='textpage',
            name='body_en',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='textpage',
            name='title_de',
            field=models.CharField(max_length=255, verbose_name=b'Header Title', blank=True),
        ),
        migrations.AddField(
            model_name='textpage',
            name='title_en',
            field=models.CharField(max_length=255, verbose_name=b'Header Title', blank=True),
        ),
        migrations.DeleteModel(
            name='StreamFieldPage',
        ),
    ]
