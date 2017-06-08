from django.db import models
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, MultiFieldPanel,
                                                ObjectList, StreamFieldPanel,
                                                TabbedInterface)
from wagtail.wagtailcore.models import Page

from contrib.translations.translations import TranslatedField

from .abstract_page_model import TranslatedStreamFieldPage


class HomePage(TranslatedStreamFieldPage):

    heading1_en = models.CharField(
        max_length=255, default="", verbose_name="Title top")
    heading1_de = models.CharField(
        max_length=255, default="", blank=True, verbose_name="Title top")

    heading2_en = models.CharField(
        max_length=255, default="", verbose_name="Title bottom")
    heading2_de = models.CharField(
        max_length=255, default="", blank=True, verbose_name="Title bottom")

    translated_heading1 = TranslatedField(
        'heading1_de',
        'heading1_en',
    )

    translated_heading2 = TranslatedField(
        'heading2_de',
        'heading2_en',
    )

    en_content_panels = [
        FieldPanel('heading1_en'),
        FieldPanel('heading2_en'),
        FieldPanel('intro_en'),
        StreamFieldPanel('body_en'),
    ]

    de_content_panels = [
        FieldPanel('heading1_de'),
        FieldPanel('heading2_de'),
        FieldPanel('intro_de'),
        StreamFieldPanel('body_de'),
    ]

    promote_panels = [
        MultiFieldPanel([
            FieldPanel('slug'),
            FieldPanel('title'),
        ],
            heading="Slug and CMS Page Name"),
        MultiFieldPanel([
            FieldPanel('seo_title'),
            FieldPanel('search_description'),
        ],
            heading="SEO settings de",
            classname="collapsible")
    ]

    edit_handler = TabbedInterface([
        ObjectList(en_content_panels, heading='English'),
        ObjectList(de_content_panels, heading='German'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings',
                   classname="settings"),
    ])

    subpage_types = ['JoinUsPage', 'TextPage',
                     'projects.ProjectIndexPage', 'blog.BlogIndexPage']
