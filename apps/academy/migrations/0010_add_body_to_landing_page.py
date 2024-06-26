# Generated by Django 3.2.13 on 2022-08-23 10:38

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("academy", "0009_academylandingpage"),
    ]

    operations = [
        migrations.AddField(
            model_name="academylandingpage",
            name="body_de",
            field=wagtail.fields.StreamField(
                [
                    (
                        "single_teaser",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "category",
                                    wagtail.blocks.CharBlock(
                                        length=32, required=False
                                    ),
                                ),
                                (
                                    "headline",
                                    wagtail.blocks.CharBlock(
                                        length=74, required=True
                                    ),
                                ),
                                (
                                    "body_text",
                                    wagtail.blocks.TextBlock(
                                        length=164, required=True
                                    ),
                                ),
                                (
                                    "link",
                                    wagtail.blocks.PageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "external_link",
                                    wagtail.blocks.URLBlock(
                                        help_text="The external link overwrites the link to a local page.",
                                        label="External Link",
                                        required=False,
                                    ),
                                ),
                                (
                                    "link_text",
                                    wagtail.blocks.CharBlock(
                                        length=24, required=True
                                    ),
                                ),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=True
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=True,
                verbose_name="Body",
            ),
        ),
        migrations.AddField(
            model_name="academylandingpage",
            name="body_en",
            field=wagtail.fields.StreamField(
                [
                    (
                        "single_teaser",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "category",
                                    wagtail.blocks.CharBlock(
                                        length=32, required=False
                                    ),
                                ),
                                (
                                    "headline",
                                    wagtail.blocks.CharBlock(
                                        length=74, required=True
                                    ),
                                ),
                                (
                                    "body_text",
                                    wagtail.blocks.TextBlock(
                                        length=164, required=True
                                    ),
                                ),
                                (
                                    "link",
                                    wagtail.blocks.PageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "external_link",
                                    wagtail.blocks.URLBlock(
                                        help_text="The external link overwrites the link to a local page.",
                                        label="External Link",
                                        required=False,
                                    ),
                                ),
                                (
                                    "link_text",
                                    wagtail.blocks.CharBlock(
                                        length=24, required=True
                                    ),
                                ),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=True
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                null=True,
                use_json_field=True,
                verbose_name="Body",
            ),
        ),
    ]
