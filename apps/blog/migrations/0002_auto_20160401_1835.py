# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.images.blocks
import wagtail.core.fields
import wagtail.core.blocks
import wagtail.embeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpagetag',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='blogpagetag',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='blogparagraph',
            name='page',
        ),
        migrations.AlterModelOptions(
            name='blogindexpage',
            options={'verbose_name': 'Blog Index Page'},
        ),
        migrations.AlterModelOptions(
            name='blogpage',
            options={'verbose_name': 'Blog Entry'},
        ),
        migrations.RenameField(
            model_name='blogpage',
            old_name='author_string',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='blogindexpage',
            name='intro',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='body',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='body_de',
            field=wagtail.core.fields.StreamField([(b'standard_paragraph', wagtail.core.blocks.StructBlock([(b'headline', wagtail.core.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.core.blocks.RichTextBlock(required=True))])), (b'highlight_paragraph', wagtail.core.blocks.StructBlock([(b'headline', wagtail.core.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.core.blocks.RichTextBlock(required=True)), (b'link', wagtail.core.blocks.PageChooserBlock(required=False))])), (b'quote_paragraph', wagtail.core.blocks.StructBlock([(b'text', wagtail.core.blocks.RichTextBlock(required=True)), (b'color', wagtail.core.blocks.ChoiceBlock(help_text=b'Select a color from the list.', required=False, choices=[(b'green', b'Gruen'), (b'orange', b'Orange'), (b'red', b'Rot')])), (b'image', wagtail.images.blocks.ImageChooserBlock(help_text=b'Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), (b'author', wagtail.core.blocks.CharBlock(length=256, required=False))])), (b'single_image', wagtail.images.blocks.ImageChooserBlock(icon=b'image', template=b'blocks/block_image.html', label=b'Single image')), (b'image_slider', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(), help_text=b'Responsive image slider (swipe on mobile). Please choose 4 images.', icon=b'image', template=b'blocks/block_carousel.html', label=b'Image Slider')), (b'columns', wagtail.core.blocks.StructBlock([(b'col1_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), (b'col1_text', wagtail.core.blocks.RichTextBlock(required=True)), (b'col2_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), (b'col2_text', wagtail.core.blocks.RichTextBlock(required=True))])), (b'linkbox', wagtail.core.blocks.StructBlock([(b'headline', wagtail.core.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.core.blocks.RichTextBlock(required=False)), (b'links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([(b'internal_link', wagtail.core.blocks.PageChooserBlock()), (b'link_text', wagtail.core.blocks.CharBlock(length=256))])))])), (b'project_teaser', wagtail.core.blocks.StructBlock([(b'translated_title', wagtail.core.blocks.CharBlock(length=256, required=False)), (b'translated_shorttext', wagtail.core.blocks.RichTextBlock(required=True)), (b'image', wagtail.images.blocks.ImageChooserBlock(icon=b'image')), (b'internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.core.blocks.URLBlock(length=256, required=False))])), (b'ThreeImageLinks', wagtail.core.blocks.StructBlock([(b'image_left', wagtail.core.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock(required=True, label=b'Image')), (b'internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), (b'link_text', wagtail.core.blocks.CharBlock(length=256))], required=True)), (b'image_middle', wagtail.core.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock(required=True, label=b'Image')), (b'internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), (b'link_text', wagtail.core.blocks.CharBlock(length=256))], required=True)), (b'image_right', wagtail.core.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock(required=True, label=b'Image')), (b'internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), (b'link_text', wagtail.core.blocks.CharBlock(length=256))], required=True))]))], null=True, verbose_name=b'Body', blank=True),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='body_en',
            field=wagtail.core.fields.StreamField([(b'standard_paragraph', wagtail.core.blocks.StructBlock([(b'headline', wagtail.core.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.core.blocks.RichTextBlock(required=True))])), (b'highlight_paragraph', wagtail.core.blocks.StructBlock([(b'headline', wagtail.core.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.core.blocks.RichTextBlock(required=True)), (b'link', wagtail.core.blocks.PageChooserBlock(required=False))])), (b'quote_paragraph', wagtail.core.blocks.StructBlock([(b'text', wagtail.core.blocks.RichTextBlock(required=True)), (b'color', wagtail.core.blocks.ChoiceBlock(help_text=b'Select a color from the list.', required=False, choices=[(b'green', b'Gruen'), (b'orange', b'Orange'), (b'red', b'Rot')])), (b'image', wagtail.images.blocks.ImageChooserBlock(help_text=b'Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), (b'author', wagtail.core.blocks.CharBlock(length=256, required=False))])), (b'single_image', wagtail.images.blocks.ImageChooserBlock(icon=b'image', template=b'blocks/block_image.html', label=b'Single image')), (b'image_slider', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(), help_text=b'Responsive image slider (swipe on mobile). Please choose 4 images.', icon=b'image', template=b'blocks/block_carousel.html', label=b'Image Slider')), (b'columns', wagtail.core.blocks.StructBlock([(b'col1_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), (b'col1_text', wagtail.core.blocks.RichTextBlock(required=True)), (b'col2_headline', wagtail.core.blocks.CharBlock(length=256, required=False)), (b'col2_text', wagtail.core.blocks.RichTextBlock(required=True))])), (b'linkbox', wagtail.core.blocks.StructBlock([(b'headline', wagtail.core.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.core.blocks.RichTextBlock(required=False)), (b'links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([(b'internal_link', wagtail.core.blocks.PageChooserBlock()), (b'link_text', wagtail.core.blocks.CharBlock(length=256))])))])), (b'project_teaser', wagtail.core.blocks.StructBlock([(b'translated_title', wagtail.core.blocks.CharBlock(length=256, required=False)), (b'translated_shorttext', wagtail.core.blocks.RichTextBlock(required=True)), (b'image', wagtail.images.blocks.ImageChooserBlock(icon=b'image')), (b'internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.core.blocks.URLBlock(length=256, required=False))])), (b'ThreeImageLinks', wagtail.core.blocks.StructBlock([(b'image_left', wagtail.core.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock(required=True, label=b'Image')), (b'internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), (b'link_text', wagtail.core.blocks.CharBlock(length=256))], required=True)), (b'image_middle', wagtail.core.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock(required=True, label=b'Image')), (b'internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), (b'link_text', wagtail.core.blocks.CharBlock(length=256))], required=True)), (b'image_right', wagtail.core.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock(required=True, label=b'Image')), (b'internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), (b'external_url', wagtail.core.blocks.URLBlock(length=256, required=False)), (b'link_text', wagtail.core.blocks.CharBlock(length=256))], required=True))]))], null=True, verbose_name=b'Body'),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='intro_de',
            field=wagtail.core.fields.RichTextField(verbose_name=b'Teasertext', blank=True),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='intro_en',
            field=wagtail.core.fields.RichTextField(verbose_name=b'Teasertext', blank=True),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='title_de',
            field=models.CharField(max_length=255, verbose_name=b'Title', blank=True),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='title_en',
            field=models.CharField(default='title', max_length=255, verbose_name=b'Title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpage',
            name='body_de',
            field=wagtail.core.fields.StreamField([(b'heading', wagtail.core.blocks.CharBlock(classname=b'full title', icon=b'title')), (b'paragraph', wagtail.core.blocks.RichTextBlock(icon=b'pilcrow')), (b'image', wagtail.images.blocks.ImageChooserBlock(icon=b'image')), (b'video', wagtail.embeds.blocks.EmbedBlock(icon=b'media'))], null=True, verbose_name=b'Body', blank=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='body_en',
            field=wagtail.core.fields.StreamField([(b'heading', wagtail.core.blocks.CharBlock(classname=b'full title', icon=b'title')), (b'paragraph', wagtail.core.blocks.RichTextBlock(icon=b'pilcrow')), (b'image', wagtail.images.blocks.ImageChooserBlock(icon=b'image')), (b'video', wagtail.embeds.blocks.EmbedBlock(icon=b'media'))], null=True, verbose_name=b'Body'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='intro_de',
            field=wagtail.core.fields.RichTextField(verbose_name=b'Teasertext', blank=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='intro_en',
            field=wagtail.core.fields.RichTextField(default='intro', verbose_name=b'Teasertext'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpage',
            name='subtitle_de',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'Subtitle', blank=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='subtitle_en',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'Subtitle'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='title_de',
            field=models.CharField(max_length=255, verbose_name=b'Title', blank=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='title_en',
            field=models.CharField(default='title', max_length=255, verbose_name=b'Title'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='BlogPageTag',
        ),
        migrations.DeleteModel(
            name='BlogParagraph',
        ),
    ]
