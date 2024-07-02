from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import MultiFieldPanel
from wagtail.admin.panels import ObjectList
from wagtail.admin.panels import TabbedInterface
from wagtail.fields import RichTextField
from wagtail.models import Page

from contrib.translations.translations import TranslatedField


class TextPage(Page):
    title_en = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title"
    )
    title_de = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title"
    )

    body_en = RichTextField(blank=True)
    body_de = RichTextField(blank=True)

    body = TranslatedField("body_de", "body_en")

    translated_title = TranslatedField(
        "title_de",
        "title_en",
    )

    content_panels = Page.content_panels + [
        FieldPanel("title"),
    ]

    de_content_panels = [
        FieldPanel("title_de"),
        FieldPanel("body_de"),
    ]

    en_content_panels = [
        FieldPanel("title_en"),
        FieldPanel("body_en"),
    ]

    promote_panels = [
        MultiFieldPanel(
            [
                FieldPanel("title"),
                FieldPanel("slug"),
            ],
            heading="Slug and CMS Page Name",
        ),
        MultiFieldPanel(
            [
                FieldPanel("seo_title"),
                FieldPanel("search_description"),
            ],
            heading="SEO settings",
            classname="collapsible",
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(en_content_panels, heading="Content en"),
            ObjectList(de_content_panels, heading="Content de"),
            ObjectList(promote_panels, heading="Promote"),
            ObjectList(
                Page.settings_panels, heading="Settings", classname="settings"
            ),
        ]
    )

    subpage_types = ["TextPage"]
