# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-21 13:24
from __future__ import unicode_literals

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_remove-person-bg"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpage",
            name="body_de",
            field=wagtail.fields.StreamField(
                (
                    (
                        "heading",
                        wagtail.blocks.CharBlock(
                            classname="full title", icon="title"
                        ),
                    ),
                    (
                        "paragraph",
                        wagtail.blocks.RichTextBlock(icon="pilcrow"),
                    ),
                    (
                        "image",
                        wagtail.images.blocks.ImageChooserBlock(icon="image"),
                    ),
                    (
                        "aligned_image",
                        wagtail.blocks.StructBlock(
                            (
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        label="Image"
                                    ),
                                ),
                                (
                                    "display",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("left", "left"),
                                            ("right", "right"),
                                        ],
                                        help_text="Decide on which side the image should be displayed",
                                    ),
                                ),
                            ),
                            icon="image",
                        ),
                    ),
                    ("video", wagtail.embeds.blocks.EmbedBlock(icon="media")),
                    (
                        "Raw_HTML",
                        wagtail.blocks.StructBlock(
                            (
                                (
                                    "headline",
                                    wagtail.blocks.CharBlock(
                                        length=256, required=False
                                    ),
                                ),
                                ("body", wagtail.blocks.RawHTMLBlock()),
                            )
                        ),
                    ),
                ),
                blank=True,
                null=True,
                verbose_name="Body",
            ),
        ),
        migrations.AlterField(
            model_name="blogpage",
            name="body_en",
            field=wagtail.fields.StreamField(
                (
                    (
                        "heading",
                        wagtail.blocks.CharBlock(
                            classname="full title", icon="title"
                        ),
                    ),
                    (
                        "paragraph",
                        wagtail.blocks.RichTextBlock(icon="pilcrow"),
                    ),
                    (
                        "image",
                        wagtail.images.blocks.ImageChooserBlock(icon="image"),
                    ),
                    (
                        "aligned_image",
                        wagtail.blocks.StructBlock(
                            (
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        label="Image"
                                    ),
                                ),
                                (
                                    "display",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("left", "left"),
                                            ("right", "right"),
                                        ],
                                        help_text="Decide on which side the image should be displayed",
                                    ),
                                ),
                            ),
                            icon="image",
                        ),
                    ),
                    ("video", wagtail.embeds.blocks.EmbedBlock(icon="media")),
                    (
                        "Raw_HTML",
                        wagtail.blocks.StructBlock(
                            (
                                (
                                    "headline",
                                    wagtail.blocks.CharBlock(
                                        length=256, required=False
                                    ),
                                ),
                                ("body", wagtail.blocks.RawHTMLBlock()),
                            )
                        ),
                    ),
                ),
                null=True,
                verbose_name="Body",
            ),
        ),
    ]
