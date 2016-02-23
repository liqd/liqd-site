# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('streampage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joinuspage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'standard_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))], template=b'blocks/block_standard_paragraph.html', icon=b'pilcrow')), (b'highlight_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))], template=b'blocks/block_highlight_paragraph.html', icon=b'pilcrow')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'columns', wagtail.wagtailcore.blocks.StructBlock([(b'col1_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=True)), (b'col1_text', wagtail.wagtailcore.blocks.RichTextBlock()), (b'col2_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=True)), (b'col2_text', wagtail.wagtailcore.blocks.RichTextBlock())], template=b'blocks/block_column.html', icon=b'grip')), (b'carousel', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailimages.blocks.ImageChooserBlock(), help_text=b'Please choose up to 4 images.', template=b'blocks/block_carousel.html', icon=b'image')), (b'linkbox', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.PageChooserBlock(), template=b'blocks/block_internalLink.html'))], template=b'blocks/block_linkbox.html', icon=b'link'))]),
        ),
        migrations.AlterField(
            model_name='joinuspage',
            name='body_de',
            field=wagtail.wagtailcore.fields.StreamField([(b'standard_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))], template=b'blocks/block_standard_paragraph.html', icon=b'pilcrow')), (b'highlight_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))], template=b'blocks/block_highlight_paragraph.html', icon=b'pilcrow')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'columns', wagtail.wagtailcore.blocks.StructBlock([(b'col1_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=True)), (b'col1_text', wagtail.wagtailcore.blocks.RichTextBlock()), (b'col2_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=True)), (b'col2_text', wagtail.wagtailcore.blocks.RichTextBlock())], template=b'blocks/block_column.html', icon=b'grip')), (b'carousel', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailimages.blocks.ImageChooserBlock(), help_text=b'Please choose up to 4 images.', template=b'blocks/block_carousel.html', icon=b'image')), (b'linkbox', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.PageChooserBlock(), template=b'blocks/block_internalLink.html'))], template=b'blocks/block_linkbox.html', icon=b'link'))], null=True),
        ),
        migrations.AlterField(
            model_name='joinuspage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField([(b'standard_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))], template=b'blocks/block_standard_paragraph.html', icon=b'pilcrow')), (b'highlight_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))], template=b'blocks/block_highlight_paragraph.html', icon=b'pilcrow')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'columns', wagtail.wagtailcore.blocks.StructBlock([(b'col1_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=True)), (b'col1_text', wagtail.wagtailcore.blocks.RichTextBlock()), (b'col2_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=True)), (b'col2_text', wagtail.wagtailcore.blocks.RichTextBlock())], template=b'blocks/block_column.html', icon=b'grip')), (b'carousel', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailimages.blocks.ImageChooserBlock(), help_text=b'Please choose up to 4 images.', template=b'blocks/block_carousel.html', icon=b'image')), (b'linkbox', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.PageChooserBlock(), template=b'blocks/block_internalLink.html'))], template=b'blocks/block_linkbox.html', icon=b'link'))], null=True),
        ),
    ]
