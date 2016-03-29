# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('core', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinUsPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('title_en', models.CharField(max_length=255, verbose_name=b'Header Title', blank=True)),
                ('title_de', models.CharField(max_length=255, verbose_name=b'Header Title', blank=True)),
                ('intro_en', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('intro_de', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('body_en', wagtail.wagtailcore.fields.StreamField([(b'standard_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))])), (b'highlight_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))])), (b'quote_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'color', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Select a color from the list.', required=False, choices=[(b'green', b'Gruen'), (b'orange', b'Orange'), (b'red', b'Rot')])), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text=b'Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), (b'author', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False))])), (b'single_image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image', template=b'blocks/block_image.html', label=b'Single image')), (b'image_slider', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailimages.blocks.ImageChooserBlock(), help_text=b'Responsive image slider (swipe on mobile). Please choose 4 images.', icon=b'image', template=b'blocks/block_carousel.html', label=b'Image Slider')), (b'columns', wagtail.wagtailcore.blocks.StructBlock([(b'col1_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'col1_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'col2_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'col2_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))])), (b'linkbox', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock()), (b'link_text', wagtail.wagtailcore.blocks.CharBlock(length=256))])))])), (b'project_teaser', wagtail.wagtailcore.blocks.StructBlock([(b'translated_title', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'translated_shorttext', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'translated_image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'translated_external_url', wagtail.wagtailcore.blocks.URLBlock(length=256, required=False))]))], null=True)),
                ('body_de', wagtail.wagtailcore.fields.StreamField([(b'standard_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))])), (b'highlight_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))])), (b'quote_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'color', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Select a color from the list.', required=False, choices=[(b'green', b'Gruen'), (b'orange', b'Orange'), (b'red', b'Rot')])), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text=b'Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), (b'author', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False))])), (b'single_image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image', template=b'blocks/block_image.html', label=b'Single image')), (b'image_slider', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailimages.blocks.ImageChooserBlock(), help_text=b'Responsive image slider (swipe on mobile). Please choose 4 images.', icon=b'image', template=b'blocks/block_carousel.html', label=b'Image Slider')), (b'columns', wagtail.wagtailcore.blocks.StructBlock([(b'col1_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'col1_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'col2_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'col2_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))])), (b'linkbox', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock()), (b'link_text', wagtail.wagtailcore.blocks.CharBlock(length=256))])))])), (b'project_teaser', wagtail.wagtailcore.blocks.StructBlock([(b'translated_title', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'translated_shorttext', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'translated_image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'translated_external_url', wagtail.wagtailcore.blocks.URLBlock(length=256, required=False))]))], null=True, blank=True)),
            ],
            options={
                'verbose_name': 'default header and streamfield',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='LiqdSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('liqd_preliminary_site', models.BooleanField(default=False, help_text=b'Phase One of the new site, this setting can be deleted when the full site is ready to go live')),
                ('site', models.OneToOneField(editable=False, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('menu_title_de', models.CharField(max_length=255, verbose_name=b'Menu Title de')),
                ('menu_title_en', models.CharField(max_length=255, verbose_name=b'Menu Title en', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NavigationMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('menu_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PressLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(null=True)),
                ('source', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField(verbose_name=b'Post date')),
            ],
        ),
        migrations.CreateModel(
            name='PressPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='TextPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('title_en', models.CharField(max_length=255, verbose_name=b'Header Title', blank=True)),
                ('title_de', models.CharField(max_length=255, verbose_name=b'Header Title', blank=True)),
                ('body_en', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('body_de', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterModelOptions(
            name='homepage',
            options={'managed': True, 'verbose_name': 'Extended Page'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_de',
            field=wagtail.wagtailcore.fields.StreamField([(b'standard_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))])), (b'highlight_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))])), (b'quote_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'color', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Select a color from the list.', required=False, choices=[(b'green', b'Gruen'), (b'orange', b'Orange'), (b'red', b'Rot')])), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text=b'Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), (b'author', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False))])), (b'single_image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image', template=b'blocks/block_image.html', label=b'Single image')), (b'image_slider', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailimages.blocks.ImageChooserBlock(), help_text=b'Responsive image slider (swipe on mobile). Please choose 4 images.', icon=b'image', template=b'blocks/block_carousel.html', label=b'Image Slider')), (b'columns', wagtail.wagtailcore.blocks.StructBlock([(b'col1_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'col1_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'col2_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'col2_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))])), (b'linkbox', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock()), (b'link_text', wagtail.wagtailcore.blocks.CharBlock(length=256))])))])), (b'project_teaser', wagtail.wagtailcore.blocks.StructBlock([(b'translated_title', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'translated_shorttext', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'translated_image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'translated_external_url', wagtail.wagtailcore.blocks.URLBlock(length=256, required=False))]))], null=True, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField([(b'standard_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))])), (b'highlight_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False))])), (b'quote_paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'color', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Select a color from the list.', required=False, choices=[(b'green', b'Gruen'), (b'orange', b'Orange'), (b'red', b'Rot')])), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text=b'Please use an image with at least 800x400px or a similar aspect ratio.', required=False)), (b'author', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False))])), (b'single_image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image', template=b'blocks/block_image.html', label=b'Single image')), (b'image_slider', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailimages.blocks.ImageChooserBlock(), help_text=b'Responsive image slider (swipe on mobile). Please choose 4 images.', icon=b'image', template=b'blocks/block_carousel.html', label=b'Image Slider')), (b'columns', wagtail.wagtailcore.blocks.StructBlock([(b'col1_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'col1_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'col2_headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'col2_text', wagtail.wagtailcore.blocks.RichTextBlock(required=True))])), (b'linkbox', wagtail.wagtailcore.blocks.StructBlock([(b'headline', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock()), (b'link_text', wagtail.wagtailcore.blocks.CharBlock(length=256))])))])), (b'project_teaser', wagtail.wagtailcore.blocks.StructBlock([(b'translated_title', wagtail.wagtailcore.blocks.CharBlock(length=256, required=False)), (b'translated_shorttext', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), (b'translated_image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'translated_external_url', wagtail.wagtailcore.blocks.URLBlock(length=256, required=False))]))], null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='heading1_de',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='heading1_en',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='heading2_de',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='heading2_en',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro_de',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro_en',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_de',
            field=models.CharField(max_length=255, verbose_name=b'Header Title', blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_en',
            field=models.CharField(max_length=255, verbose_name=b'Header Title', blank=True),
        ),
        migrations.CreateModel(
            name='NavigationMenuItem',
            fields=[
                ('menuitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.MenuItem')),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('parent', modelcluster.fields.ParentalKey(related_name='menu_items', to='core.NavigationMenu')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('core.menuitem', models.Model),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='link_page',
            field=models.ForeignKey(related_name='+', to='wagtailcore.Page'),
        ),
    ]
