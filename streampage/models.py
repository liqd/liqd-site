from django.db import models
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailsearch import index
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel
from wagtail.wagtailadmin.edit_handlers import InlinePanel
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse

from wagtail_modeltranslation.models import TranslationMixin
from wagtail.wagtailadmin.edit_handlers import TabbedInterface, ObjectList


class StreamPage(Page):
    
    intro = RichTextField(blank=True)
    body = StreamField([
        ('standard_paragraph', blocks.StructBlock(
            [
                ('headline', blocks.CharBlock(required=False, length=256)),
                ('text', blocks.RichTextBlock(required=True)),
            ], template="blocks/block_standard_paragraph.html", icon="pilcrow")
        ),
        ('highlight_paragraph', blocks.StructBlock(
            [
                ('headline', blocks.CharBlock(required=False, length=256)),
                ('text', blocks.RichTextBlock(required=True)),
                ('link', blocks.PageChooserBlock(required=False)),
            ], template="blocks/block_highlight_paragraph.html", icon="pilcrow")
        ),
        ('image', ImageChooserBlock(icon="image"), ),
        ('columns', blocks.StructBlock(
            [
                ('col1_headline', blocks.CharBlock(required=True, length=256)),
                ('col1_text', blocks.RichTextBlock()),
                ('col2_headline', blocks.CharBlock(required=True, length=256)),
                ('col2_text', blocks.RichTextBlock()),
            ], template = "blocks/block_column.html", icon="grip")
        ),
        ('carousel', blocks.ListBlock(
            ImageChooserBlock(), 
            template = "blocks/block_carousel.html",
            help_text = "Please choose up to 4 images.",
            icon="image"
            ),
        ),
        ('linkbox', blocks.StructBlock(
            [
                ('headline', blocks.CharBlock(required=False, length=256)),
                ('links', blocks.ListBlock(
                    blocks.PageChooserBlock(),
                    template = "blocks/block_internalLink.html"
                    ),
                ),
                
            ], template = "blocks/block_linkbox.html", icon="link")
        ),('project_teaser', blocks.StructBlock(
            [
                ('title', blocks.CharBlock(required=False, length=256)),
                ('shorttext', blocks.RichTextBlock(required=True)),
                ('image', ImageChooserBlock(icon="image")),
                ('slug', blocks.ListBlock(
                    blocks.PageChooserBlock(),
                    template = "blocks/block_internalLink.html",
                    required=False
                    ),
                ),
                ('external_url', blocks.CharBlock(required=False, length=256)),
            ], template="blocks/block_project_teaser.html", icon="")
        ),
    ])

    de_content_panels = [
        FieldPanel('title_de'),
        FieldPanel('intro_de'),
        StreamFieldPanel('body_de'),
    ]

    en_content_panels = [
        FieldPanel('title_en'),
        FieldPanel('intro_en'),
        StreamFieldPanel('body_en'),
    ]

    promote_panels = [
        FieldPanel('slug'),
        MultiFieldPanel([
            FieldPanel('seo_title_de'),
            FieldPanel('search_description_de'),
        ],
        heading = "SEO settings de",
        classname="collapsible"),
        MultiFieldPanel([
            FieldPanel('seo_title_en'),
            FieldPanel('search_description_en'),
        ],
        heading = "SEO settings en",
        classname="collapsible")
    ]

    edit_handler = TabbedInterface([
        # ObjectList(content_panels, heading='Content'),
        ObjectList(de_content_panels, heading='Content de'),
        ObjectList(en_content_panels, heading='Content en'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    ])

    class Meta:
        verbose_name = 'Stream Page'
        managed = True
        abstract = True


class JoinUsPage(TranslationMixin, StreamPage):
    content_panels = [
    ]

    class Meta:
        verbose_name = 'JoinUs Page'
