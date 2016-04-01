# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20160330_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectpersons',
            name='page',
        ),
        migrations.RemoveField(
            model_name='projectpersons',
            name='person',
        ),
        migrations.AlterModelOptions(
            name='projectpage',
            options={'verbose_name': 'Project'},
        ),
        migrations.RenameField(
            model_name='projectpage',
            old_name='streamFieldBottom_de',
            new_name='body_de',
        ),
        migrations.RenameField(
            model_name='projectpage',
            old_name='streamFieldTop_en',
            new_name='body_en',
        ),
        migrations.RenameField(
            model_name='projectpage',
            old_name='external_url_de',
            new_name='external_url',
        ),
        migrations.RenameField(
            model_name='projectpage',
            old_name='image_en',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='projectpage',
            name='external_url_en',
        ),
        migrations.RemoveField(
            model_name='projectpage',
            name='image_de',
        ),
        migrations.RemoveField(
            model_name='projectpage',
            name='streamFieldBottom_en',
        ),
        migrations.RemoveField(
            model_name='projectpage',
            name='streamFieldTop_de',
        ),
        migrations.AlterField(
            model_name='projectindexpage',
            name='body_de',
            field=wagtail.wagtailcore.fields.StreamField([(b'standard_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))])), (b'highlight_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))])), (b'quote_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'color', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Select a color from the list.', required=False, choices=[(b'green', b'Gruen'), (b'orange', b'Orange'), (b'red', b'Rot')])), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text=b'Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), (b'author', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False))])), (b'single_image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image', template=b'blocks/block_image.html', label=b'Single image')), (b'image_slider', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailimages.blocks.ImageChooserBlock(), help_text=b'Responsive image slider (swipe on mobile). Please choose 4 images.', icon=b'image', template=b'blocks/block_carousel.html', label=b'Image Slider')), (b'columns', wagtail.wagtailcore.blocks.StructBlock([(b'col1_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'col1_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'col2_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'col2_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))])), (b'linkbox', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock()), (b'link_text', wagtail.wagtailcore.blocks.CharBlock(length=256))])))])), (b'project_teaser', wagtail.wagtailcore.blocks.StructBlock([(b'translated_title', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'translated_shorttext', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'translated_image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'translated_external_url', wagtail.wagtailcore.blocks.URLBlock(length=256, required=False))])), (b'ThreeImageLinks', wagtail.wagtailcore.blocks.StructBlock([(b'image_left', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True, label=b'Image')), (b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.wagtailcore.blocks.URLBlock(length=256, required=False)), (b'link_text', wagtail.wagtailcore.blocks.CharBlock(length=256))], required=True)), (b'image_middle', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True, label=b'Image')), (b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.wagtailcore.blocks.URLBlock(length=256, required=False)), (b'link_text', wagtail.wagtailcore.blocks.CharBlock(length=256))], required=True)), (b'image_right', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True, label=b'Image')), (b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.wagtailcore.blocks.URLBlock(length=256, required=False)), (b'link_text', wagtail.wagtailcore.blocks.CharBlock(length=256))], required=True))]))], null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='projectindexpage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField([(b'standard_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))])), (b'highlight_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))])), (b'quote_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'color', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Select a color from the list.', required=False, choices=[(b'green', b'Gruen'), (b'orange', b'Orange'), (b'red', b'Rot')])), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text=b'Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), (b'author', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False))])), (b'single_image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image', template=b'blocks/block_image.html', label=b'Single image')), (b'image_slider', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailimages.blocks.ImageChooserBlock(), help_text=b'Responsive image slider (swipe on mobile). Please choose 4 images.', icon=b'image', template=b'blocks/block_carousel.html', label=b'Image Slider')), (b'columns', wagtail.wagtailcore.blocks.StructBlock([(b'col1_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'col1_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'col2_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'col2_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))])), (b'linkbox', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock()), (b'link_text', wagtail.wagtailcore.blocks.CharBlock(length=256))])))])), (b'project_teaser', wagtail.wagtailcore.blocks.StructBlock([(b'translated_title', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'translated_shorttext', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'translated_image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'translated_external_url', wagtail.wagtailcore.blocks.URLBlock(length=256, required=False))])), (b'ThreeImageLinks', wagtail.wagtailcore.blocks.StructBlock([(b'image_left', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True, label=b'Image')), (b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.wagtailcore.blocks.URLBlock(length=256, required=False)), (b'link_text', wagtail.wagtailcore.blocks.CharBlock(length=256))], required=True)), (b'image_middle', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True, label=b'Image')), (b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.wagtailcore.blocks.URLBlock(length=256, required=False)), (b'link_text', wagtail.wagtailcore.blocks.CharBlock(length=256))], required=True)), (b'image_right', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True, label=b'Image')), (b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.wagtailcore.blocks.URLBlock(length=256, required=False)), (b'link_text', wagtail.wagtailcore.blocks.CharBlock(length=256))], required=True))]))], null=True),
        ),
        migrations.DeleteModel(
            name='ProjectPersons',
        ),
    ]
