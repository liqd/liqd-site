# Generated by Django 3.2.13 on 2022-09-06 14:54

from django.db import migrations, models
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("academy", "0017_update_filter_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="academychallengepage",
            name="body_en",
            field=wagtail.fields.StreamField(
                [
                    (
                        "challenge_tasks",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "challenge_step_title",
                                    wagtail.blocks.CharBlock(),
                                ),
                                (
                                    "challenge_step_text",
                                    wagtail.blocks.RichTextBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "links",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "challenge_step_academy_links",
                                                    wagtail.blocks.PageChooserBlock(
                                                        help_text="Add link to a challenge page either internal or external",
                                                        page_type=[
                                                            "academy.AcademyPage"
                                                        ],
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "challenge_step_external_links",
                                                    wagtail.blocks.PageChooserBlock(
                                                        page_type=[
                                                            "academy.AcademyExternalLink"
                                                        ],
                                                        required=False,
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=True,
                verbose_name="Challenge step",
            ),
        ),
        migrations.AlterField(
            model_name="academychallengepage",
            name="completion_time_en",
            field=models.CharField(
                blank=True, max_length=500, verbose_name="Time to complete"
            ),
        ),
        migrations.AlterField(
            model_name="academychallengepage",
            name="intro_en",
            field=wagtail.fields.RichTextField(
                blank=True, verbose_name="Teaser text"
            ),
        ),
        migrations.AlterField(
            model_name="academychallengepage",
            name="subtitle_en",
            field=models.CharField(
                blank=True, max_length=500, verbose_name="Subtitle"
            ),
        ),
        migrations.AlterField(
            model_name="academychallengepage",
            name="title_en",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Title"
            ),
        ),
        migrations.AlterField(
            model_name="academyexternallink",
            name="intro_en",
            field=wagtail.fields.RichTextField(
                blank=True, verbose_name="Teasertext"
            ),
        ),
        migrations.AlterField(
            model_name="academyexternallink",
            name="title_de",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Title de"
            ),
        ),
        migrations.AlterField(
            model_name="academyexternallink",
            name="title_en",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Title en"
            ),
        ),
        migrations.AlterField(
            model_name="academyindexpage",
            name="title_en",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Title"
            ),
        ),
        migrations.AlterField(
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
                                        max_length=32, required=False
                                    ),
                                ),
                                (
                                    "headline",
                                    wagtail.blocks.CharBlock(
                                        max_length=74, required=True
                                    ),
                                ),
                                (
                                    "body_text",
                                    wagtail.blocks.TextBlock(
                                        max_length=164, required=True
                                    ),
                                ),
                                (
                                    "link",
                                    wagtail.blocks.PageChooserBlock(
                                        help_text="Please only add either an internal or external link",
                                        required=False,
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
                                        max_length=24, required=True
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
                    ),
                    (
                        "call_to_action_teaser",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "columns",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "headline",
                                                    wagtail.blocks.CharBlock(
                                                        max_length=28,
                                                        required=True,
                                                    ),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        help_text="Please add image with transparent background",
                                                        required=True,
                                                    ),
                                                ),
                                                (
                                                    "body_text",
                                                    wagtail.blocks.TextBlock(
                                                        max_length=120,
                                                        required=True,
                                                    ),
                                                ),
                                                (
                                                    "cta_link",
                                                    wagtail.blocks.StructBlock(
                                                        [
                                                            (
                                                                "internal_link",
                                                                wagtail.blocks.PageChooserBlock(
                                                                    help_text="The external link overwrites the link to a local page. Please only add 1 link.",
                                                                    required=False,
                                                                ),
                                                            ),
                                                            (
                                                                "external_link",
                                                                wagtail.blocks.URLBlock(
                                                                    required=False
                                                                ),
                                                            ),
                                                        ]
                                                    ),
                                                ),
                                                (
                                                    "link_text",
                                                    wagtail.blocks.CharBlock(
                                                        label="Link Text",
                                                        max_length=28,
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "anchor_link",
                                                    wagtail.blocks.CharBlock(
                                                        help_text="Anchor link should be all one word.",
                                                        label="Anchor Link",
                                                        max_length=28,
                                                        required=False,
                                                    ),
                                                ),
                                            ],
                                            label="List and Image",
                                        ),
                                        max_num=2,
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "topic_block_list",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        max_length=74, required=True
                                    ),
                                ),
                                (
                                    "topics",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "topic_category",
                                                    wagtail.blocks.ChoiceBlock(
                                                        choices=[
                                                            (
                                                                "LT",
                                                                "Liquid Democracy: Theory & Vision",
                                                            ),
                                                            (
                                                                "DS",
                                                                "Digital Civic Society",
                                                            ),
                                                            (
                                                                "PA",
                                                                "Digital Participation In Action",
                                                            ),
                                                        ],
                                                        help_text="Select a topic",
                                                    ),
                                                ),
                                                (
                                                    "topic_text",
                                                    wagtail.blocks.CharBlock(
                                                        max_length=110,
                                                        required=True,
                                                    ),
                                                ),
                                                (
                                                    "topic_link_text",
                                                    wagtail.blocks.CharBlock(
                                                        max_length=40,
                                                        required=True,
                                                    ),
                                                ),
                                            ]
                                        ),
                                        max_num=3,
                                        min_num=3,
                                    ),
                                ),
                                (
                                    "topic_url",
                                    wagtail.blocks.PageChooserBlock(
                                        page_type=["academy.AcademyIndexPage"],
                                        required=True,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "teaser_columns",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "headline",
                                    wagtail.blocks.CharBlock(
                                        max_length=74, required=True
                                    ),
                                ),
                                (
                                    "teasers",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "link",
                                                    wagtail.blocks.PageChooserBlock(
                                                        page_type=[
                                                            "academy.AcademyPage",
                                                            "academy.AcademyExternalLink",
                                                            "academy.AcademyChallengePage",
                                                        ],
                                                        required=True,
                                                    ),
                                                )
                                            ]
                                        ),
                                        max_num=3,
                                        min_num=2,
                                    ),
                                ),
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
                use_json_field=True,
                verbose_name="Body",
            ),
        ),
        migrations.AlterField(
            model_name="academylandingpage",
            name="intro_text_en",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="intro text en"
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
                            form_classname="full title", icon="title"
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
                                        max_length=256, required=False
                                    ),
                                ),
                                ("body", wagtail.blocks.RawHTMLBlock()),
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
                use_json_field=True,
                verbose_name="Body",
            ),
        ),
        migrations.AlterField(
            model_name="academypage",
            name="subtitle_en",
            field=models.CharField(
                blank=True, default="", max_length=255, verbose_name="Subtitle"
            ),
        ),
        migrations.AlterField(
            model_name="academypage",
            name="title_en",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Title"
            ),
        ),
    ]
