from wagtail.wagtailcore.models import Page
from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailsnippets.models import register_snippet


class HomePage(Page):
    pass


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
