# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20150612_1514'),
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
        migrations.DeleteModel(
            name='ProjectParagraphBottom',
        ),
        migrations.RemoveField(
            model_name='projectparagraphtop',
            name='image',
        ),
        migrations.RemoveField(
            model_name='projectparagraphtop',
            name='page',
        ),
        migrations.DeleteModel(
            name='ProjectParagraphTop',
        ),
        migrations.AddField(
            model_name='projectpage',
            name='streamFieldBottom',
            field=wagtail.wagtailcore.fields.StreamField([(b'heading', wagtail.wagtailcore.blocks.CharBlock(classname=b'full title', icon=b'title')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'pilcrow')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image'))], null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projectpage',
            name='streamFieldTop',
            field=wagtail.wagtailcore.fields.StreamField([(b'heading', wagtail.wagtailcore.blocks.CharBlock(classname=b'full title', icon=b'title')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'pilcrow')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image'))], null=True),
            preserve_default=True,
        ),
    ]
