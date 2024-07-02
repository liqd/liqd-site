# Generated by Django 2.2.9 on 2020-06-24 11:58

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("academy", "0003_rename_topic_and_contenttype"),
    ]

    operations = [
        migrations.AlterField(
            model_name="academypage",
            name="body_de",
            field=wagtail.fields.StreamField(
                [
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
                            [
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
                                            ("center", "center"),
                                            ("left", "left"),
                                            ("right", "right"),
                                        ],
                                        help_text="Decide on which side the image should be displayed",
                                    ),
                                ),
                            ],
                            icon="image",
                        ),
                    ),
                    ("video", wagtail.embeds.blocks.EmbedBlock(icon="media")),
                    (
                        "Raw_HTML",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "headline",
                                    wagtail.blocks.CharBlock(
                                        length=256, required=False
                                    ),
                                ),
                                ("body", wagtail.blocks.RawHTMLBlock()),
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
                verbose_name="Body",
            ),
        ),
        migrations.AlterField(
            model_name="academypage",
            name="body_en",
            field=wagtail.fields.StreamField(
                [
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
                            [
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
                                            ("center", "center"),
                                            ("left", "left"),
                                            ("right", "right"),
                                        ],
                                        help_text="Decide on which side the image should be displayed",
                                    ),
                                ),
                            ],
                            icon="image",
                        ),
                    ),
                    ("video", wagtail.embeds.blocks.EmbedBlock(icon="media")),
                    (
                        "Raw_HTML",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "headline",
                                    wagtail.blocks.CharBlock(
                                        length=256, required=False
                                    ),
                                ),
                                ("body", wagtail.blocks.RawHTMLBlock()),
                            ]
                        ),
                    ),
                ],
                null=True,
                verbose_name="Body",
            ),
        ),
    ]
