from django import forms
from django.utils.translation import ugettext_lazy as _
from django.db import models
from multiselectfield import MultiSelectField
from wagtail.admin.edit_handlers import (FieldPanel, MultiFieldPanel,
                                                ObjectList, StreamFieldPanel,
                                                TabbedInterface)
from wagtail.core.models import Page
from apps.blog.models import AbstractBlogPage

LIQDTHEORY = 'LT'
DIGITALCIVICSOCIETY = 'DS'
PARTICIPATIONACTION = 'PA'

VIDEO = 'VD'
WORKSHOP = 'WS'
TALK = 'TK'
LINKLIST = 'LL'
BLOGPOST = 'BP'
WEBINAR = 'WB'

TOPIC_CHOICES = [
    (LIQDTHEORY, _('Liquid Democracy & Theory')),
    (DIGITALCIVICSOCIETY, _('Digital Civic Society')),
    (PARTICIPATIONACTION, _('Digital Participation In Action')),
]

CONTENT_TYPE_CHOICES = [
    (VIDEO, _('video')),
    (WORKSHOP, _('workshop')),
    (TALK, _('talk')),
    (LINKLIST, _('link list')),
    (BLOGPOST, _('blogpost')),
    (WEBINAR, _('webinar')),
]


class AcademyPage(AbstractBlogPage):
    topics = MultiSelectField(
        max_length=8,
        max_choices=3,
        choices=TOPIC_CHOICES
    )

    page_content_type = models.CharField(
        max_length=2,
        choices=CONTENT_TYPE_CHOICES,
        blank=True
    )

    class Meta:
        verbose_name = 'Academy Page'

    en_content_panels = [
        FieldPanel('title_en'),
        FieldPanel('subtitle_en'),
        FieldPanel('intro_en'),
        StreamFieldPanel('body_en'),
    ]

    de_content_panels = [
        FieldPanel('title_de'),
        FieldPanel('subtitle_de'),
        FieldPanel('intro_de'),
        StreamFieldPanel('body_de'),
    ]

    common_panels = [
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('topics', widget=forms.CheckboxSelectMultiple),
        FieldPanel('page_content_type'),
    ]

    promote_panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('slug'),
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
        ObjectList(common_panels, heading='Common'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(
            Page.settings_panels, heading='Settings', classname="settings"),
    ])
