# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.images.blocks
import wagtail.fields
import wagtail.blocks
import wagtail.embeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectparagraphbottom',
            name='image',
        ),
        migrations.RemoveField(
            model_name='projectparagraphbottom',
            name='page',
        ),
        migrations.RemoveField(
            model_name='projectparagraphtop',
            name='image',
        ),
        migrations.RemoveField(
            model_name='projectparagraphtop',
            name='page',
        ),
        migrations.AlterModelOptions(
            name='projectindexpage',
            options={'verbose_name': 'ProjectIndexPage'},
        ),
        migrations.AlterModelOptions(
            name='projectpage',
            options={'verbose_name': 'Project'},
        ),
        migrations.RemoveField(
            model_name='projectindexpage',
            name='intro',
        ),
        migrations.RemoveField(
            model_name='projectpage',
            name='shorttext',
        ),
        migrations.RemoveField(
            model_name='projectpage',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='projectindexpage',
            name='body_de',
            field=wagtail.fields.StreamField([(b'standard_paragraph', wagtail.blocks.StructBlock([(b'headline', wagtail.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.blocks.RichTextBlock(required=True))])), (b'highlight_paragraph', wagtail.blocks.StructBlock([(b'headline', wagtail.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.blocks.RichTextBlock(required=True)), (b'link', wagtail.blocks.PageChooserBlock(required=False))])), (b'quote_paragraph', wagtail.blocks.StructBlock([(b'text', wagtail.blocks.RichTextBlock(required=True)), (b'color', wagtail.blocks.ChoiceBlock(help_text=b'Select a color from the list.', required=False, choices=[(b'green', b'Gruen'), (b'orange', b'Orange'), (b'red', b'Rot')])), (b'image', wagtail.images.blocks.ImageChooserBlock(help_text=b'Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), (b'author', wagtail.blocks.CharBlock(length=256, required=False))])), (b'single_image', wagtail.images.blocks.ImageChooserBlock(icon=b'image', template=b'blocks/block_image.html', label=b'Single image')), (b'image_slider', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(), help_text=b'Responsive image slider (swipe on mobile). Please choose 4 images.', icon=b'image', template=b'blocks/block_carousel.html', label=b'Image Slider')), (b'columns', wagtail.blocks.StructBlock([(b'col1_headline', wagtail.blocks.CharBlock(length=256, required=False)), (b'col1_text', wagtail.blocks.RichTextBlock(required=True)), (b'col2_headline', wagtail.blocks.CharBlock(length=256, required=False)), (b'col2_text', wagtail.blocks.RichTextBlock(required=True))])), (b'linkbox', wagtail.blocks.StructBlock([(b'headline', wagtail.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.blocks.RichTextBlock(required=False)), (b'links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([(b'internal_link', wagtail.blocks.PageChooserBlock()), (b'link_text', wagtail.blocks.CharBlock(length=256))])))])), (b'project_teaser', wagtail.blocks.StructBlock([(b'translated_title', wagtail.blocks.CharBlock(length=256, required=False)), (b'translated_shorttext', wagtail.blocks.RichTextBlock(required=True)), (b'image', wagtail.images.blocks.ImageChooserBlock(icon=b'image')), (b'internal_link', wagtail.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.blocks.URLBlock(length=256, required=False))])), (b'ThreeImageLinks', wagtail.blocks.StructBlock([(b'image_left', wagtail.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock(required=True, label=b'Image')), (b'internal_link', wagtail.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.blocks.URLBlock(length=256, required=False)), (b'link_text', wagtail.blocks.CharBlock(length=256))], required=True)), (b'image_middle', wagtail.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock(required=True, label=b'Image')), (b'internal_link', wagtail.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.blocks.URLBlock(length=256, required=False)), (b'link_text', wagtail.blocks.CharBlock(length=256))], required=True)), (b'image_right', wagtail.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock(required=True, label=b'Image')), (b'internal_link', wagtail.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.blocks.URLBlock(length=256, required=False)), (b'link_text', wagtail.blocks.CharBlock(length=256))], required=True))]))], null=True, verbose_name=b'Body', blank=True),
        ),
        migrations.AddField(
            model_name='projectindexpage',
            name='body_en',
            field=wagtail.fields.StreamField([(b'standard_paragraph', wagtail.blocks.StructBlock([(b'headline', wagtail.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.blocks.RichTextBlock(required=True))])), (b'highlight_paragraph', wagtail.blocks.StructBlock([(b'headline', wagtail.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.blocks.RichTextBlock(required=True)), (b'link', wagtail.blocks.PageChooserBlock(required=False))])), (b'quote_paragraph', wagtail.blocks.StructBlock([(b'text', wagtail.blocks.RichTextBlock(required=True)), (b'color', wagtail.blocks.ChoiceBlock(help_text=b'Select a color from the list.', required=False, choices=[(b'green', b'Gruen'), (b'orange', b'Orange'), (b'red', b'Rot')])), (b'image', wagtail.images.blocks.ImageChooserBlock(help_text=b'Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), (b'author', wagtail.blocks.CharBlock(length=256, required=False))])), (b'single_image', wagtail.images.blocks.ImageChooserBlock(icon=b'image', template=b'blocks/block_image.html', label=b'Single image')), (b'image_slider', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(), help_text=b'Responsive image slider (swipe on mobile). Please choose 4 images.', icon=b'image', template=b'blocks/block_carousel.html', label=b'Image Slider')), (b'columns', wagtail.blocks.StructBlock([(b'col1_headline', wagtail.blocks.CharBlock(length=256, required=False)), (b'col1_text', wagtail.blocks.RichTextBlock(required=True)), (b'col2_headline', wagtail.blocks.CharBlock(length=256, required=False)), (b'col2_text', wagtail.blocks.RichTextBlock(required=True))])), (b'linkbox', wagtail.blocks.StructBlock([(b'headline', wagtail.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.blocks.RichTextBlock(required=False)), (b'links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([(b'internal_link', wagtail.blocks.PageChooserBlock()), (b'link_text', wagtail.blocks.CharBlock(length=256))])))])), (b'project_teaser', wagtail.blocks.StructBlock([(b'translated_title', wagtail.blocks.CharBlock(length=256, required=False)), (b'translated_shorttext', wagtail.blocks.RichTextBlock(required=True)), (b'image', wagtail.images.blocks.ImageChooserBlock(icon=b'image')), (b'internal_link', wagtail.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.blocks.URLBlock(length=256, required=False))])), (b'ThreeImageLinks', wagtail.blocks.StructBlock([(b'image_left', wagtail.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock(required=True, label=b'Image')), (b'internal_link', wagtail.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.blocks.URLBlock(length=256, required=False)), (b'link_text', wagtail.blocks.CharBlock(length=256))], required=True)), (b'image_middle', wagtail.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock(required=True, label=b'Image')), (b'internal_link', wagtail.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.blocks.URLBlock(length=256, required=False)), (b'link_text', wagtail.blocks.CharBlock(length=256))], required=True)), (b'image_right', wagtail.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock(required=True, label=b'Image')), (b'internal_link', wagtail.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.blocks.URLBlock(length=256, required=False)), (b'link_text', wagtail.blocks.CharBlock(length=256))], required=True))]))], null=True, verbose_name=b'Body'),
        ),
        migrations.AddField(
            model_name='projectindexpage',
            name='intro_de',
            field=wagtail.fields.RichTextField(verbose_name=b'Teasertext', blank=True),
        ),
        migrations.AddField(
            model_name='projectindexpage',
            name='intro_en',
            field=wagtail.fields.RichTextField(verbose_name=b'Teasertext', blank=True),
        ),
        migrations.AddField(
            model_name='projectindexpage',
            name='title_de',
            field=models.CharField(max_length=255, verbose_name=b'Title', blank=True),
        ),
        migrations.AddField(
            model_name='projectindexpage',
            name='title_en',
            field=models.CharField(default='title', max_length=255, verbose_name=b'Title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectpage',
            name='body_de',
            field=wagtail.fields.StreamField([(b'heading', wagtail.blocks.CharBlock(classname=b'full title', icon=b'title')), (b'paragraph', wagtail.blocks.RichTextBlock(icon=b'pilcrow')), (b'image', wagtail.images.blocks.ImageChooserBlock(icon=b'image')), (b'video', wagtail.embeds.blocks.EmbedBlock(icon=b'media'))], null=True, verbose_name=b'Body', blank=True),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='body_en',
            field=wagtail.fields.StreamField([(b'heading', wagtail.blocks.CharBlock(classname=b'full title', icon=b'title')), (b'paragraph', wagtail.blocks.RichTextBlock(icon=b'pilcrow')), (b'image', wagtail.images.blocks.ImageChooserBlock(icon=b'image')), (b'video', wagtail.embeds.blocks.EmbedBlock(icon=b'media'))], null=True, verbose_name=b'Body'),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='external_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='shorttext_de',
            field=wagtail.fields.RichTextField(default=b'', max_length=300, verbose_name=b'Teasertext', blank=True),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='shorttext_en',
            field=wagtail.fields.RichTextField(default=b'', max_length=300, verbose_name=b'Teasertext', blank=True),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='subtitle_de',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'Subtitle', blank=True),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='subtitle_en',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'Subtitle', blank=True),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='title_de',
            field=models.CharField(max_length=255, verbose_name=b'Title', blank=True),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='title_en',
            field=models.CharField(default='title', max_length=255, verbose_name=b'Title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.DeleteModel(
            name='ProjectParagraphBottom',
        ),
        migrations.DeleteModel(
            name='ProjectParagraphTop',
        ),
    ]
