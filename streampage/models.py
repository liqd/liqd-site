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

from streampage import blocks

class StreamPage(Page):
    
    intro = RichTextField(blank=True)
    body = StreamField([
        ('standard_paragraph', blocks.StandardParagraphBlock()),
        ('highlight_paragraph', blocks.HighlightParagraphBlock()),
        ('quote_paragraph', blocks.QuoteParagraph()),
        ('image', ImageChooserBlock(label='Single image',icon='image')),
        ('columns', blocks.ColumnBlock()),
        ('image_slider', blocks.ListBlock(ImageChooserBlock(),
            template='blocks/block_carousel.html',
            label='Image Slider',
            icon='image',
            help_text='Responsive image slider (swipe on mobile). Please choose 4 images.')),
        ('linkbox', blocks.LinkboxBlock()),
        ('project_teaser', blocks.ProjectTeaserBlock()),
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
