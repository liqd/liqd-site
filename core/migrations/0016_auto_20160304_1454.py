# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20160229_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'standard_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))], help_text=b'Standard paragraph', template=b'blocks/block_standard_paragraph.html', icon=b'pilcrow')), (b'highlight_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))], help_text=b'Paragraph with grey background. Use this as linkbox also (e.g. job offers).', template=b'blocks/block_highlight_paragraph.html', icon=b'pilcrow')), (b'quote_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'color', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Select a color from the listself.', choices=[(b'green', b'Gruen'), (b'orange', b'Orange'), (b'red', b'Rot')]))], help_text=b'Textquote with background color.', template=b'blocks/block_quote_paragraph_image.html', icon=b'pilcrow')), (b'quote_paragraph_image', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text=b'Please use an image with at least 813x400px and a similar aspect ratio.', required=True, icon=b'image'))], help_text=b'Textquote with background image.', template=b'blocks/block_quote_paragraph_image.html', icon=b'pilcrow')), (b'project_teaser', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'shorttext', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'slug', wagtail.wagtailcore.blocks.PageChooserBlock(help_text=b'Please choose an internal page from the list.')), (b'external_url', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False))], help_text=b'Generic teaser / Project teaser with manual content', template=b'blocks/block_project_teaser.html', icon=b'pilcrow'))], null=True),
        ),
    ]
