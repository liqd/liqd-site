from wagtail.wagtailcore.models import Page
from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailsnippets.models import register_snippet

from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock

from wagtail_modeltranslation.models import TranslationMixin
from wagtail.wagtailadmin.edit_handlers import TabbedInterface, ObjectList, MultiFieldPanel

from wagtail.contrib.settings.models import BaseSetting, register_setting



class HomePage(TranslationMixin, Page):
    heading = models.CharField(max_length=255, default="")
    intro = RichTextField(blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
    ], null=True)
    content_panels = [
    ]
    de_content_panels = [
        FieldPanel('heading_de'),
        FieldPanel('intro_de'),
        StreamFieldPanel('body_de'),
    ]

    en_content_panels = [
        FieldPanel('heading_en'),
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


class TextPage(TranslationMixin, Page):
    
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
    ]

    de_content_panels = [
        FieldPanel('title_de'),
        FieldPanel('body_de'),
    ]

    en_content_panels = [
        FieldPanel('title_en'),
        FieldPanel('body_en'),
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


class PressPage(Page):
    intro = RichTextField(blank=True)

    #subpage_types = []

PressPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full")
]


@register_snippet
class PressLink(models.Model):
    url = models.URLField(null=True)
    source = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date = models.DateField("Post date")

    panels = [
        FieldPanel('url'),
        FieldPanel('source'),
        FieldPanel('title'),
        FieldPanel('date')
    ]

    def __unicode__(self):
        return self.source + ', ' + self.title


@register_setting
class LiqdSettings(BaseSetting):
    liqd_preliminary_site = models.BooleanField(
        default=False,
        help_text="Phase One of the new site, this setting can be deleted when the full site is ready to go live",
    )
