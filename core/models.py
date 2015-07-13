from wagtail.wagtailcore.models import Page
from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailsnippets.models import register_snippet

from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock


class HomePage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
    ], null=True)

HomePage.content_panels = [
    StreamFieldPanel('body')
]


class PressPage(Page):
    intro = RichTextField(blank=True)

    subpage_types = []

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
