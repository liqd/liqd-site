from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.paginator import InvalidPage, Paginator
from django.db import models
from django.db.models import Count
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from modelcluster.fields import ParentalManyToManyField
from multiselectfield import MultiSelectField
from wagtail.admin.edit_handlers import (FieldPanel, MultiFieldPanel,
                                                ObjectList, StreamFieldPanel,
                                                TabbedInterface,
                                                PageChooserPanel)
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

from apps.core.blocks import AlignedImageBlock, HTMLBlock
from apps.core.models.abstract_page_model import TranslatedStreamFieldPage
from contrib.translations.translations import TranslatedField
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

STREAMFIELD_ACADEMY_BLOCKS = [
    ('heading', blocks.CharBlock(classname="full title", icon="title")),
    ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
    ('image', ImageChooserBlock(icon="image")),
    ('aligned_image', AlignedImageBlock(icon="image")),
    ('video', EmbedBlock(icon="media")),
    ('Raw_HTML', HTMLBlock())
]


class AcademyPage(AbstractBlogPage):

<<<<<<< HEAD
    topics = MultiSelectField(
        max_length=8,
        max_choices=3,
=======
    topics = models.CharField(
        max_length=2,
>>>>>>> academy/models: remove index page for now and let AcademyPage inherit from AbstractBlogPage
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
<<<<<<< HEAD
        FieldPanel('topics', widget=forms.CheckboxSelectMultiple),
=======
        FieldPanel('topics'),
>>>>>>> academy/models: remove index page for now and let AcademyPage inherit from AbstractBlogPage
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
<<<<<<< HEAD
    ])
=======
        ObjectList(
            Page.settings_panels, heading='Settings', classname="settings"),
    ])


>>>>>>> academy/models: remove index page for now and let AcademyPage inherit from AbstractBlogPage
