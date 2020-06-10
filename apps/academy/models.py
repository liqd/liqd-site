from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.paginator import InvalidPage, Paginator
from django.db import models
from django.db.models import Count
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from modelcluster.fields import ParentalManyToManyField
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
from apps.blog.models import BlogPage as BlogPage

LIQDTHEORY = 'LT'
DIGITALCIVICSOCIETY = 'DS'
PARTICIPATIONACTION = 'PA'


TOPIC_CHOICES = [
    (LIQDTHEORY, _('Liquid Democracy & Theory')),
    (DIGITALCIVICSOCIETY, _('Digital Civic Society')),
    (PARTICIPATIONACTION, _('Digital Participation In Action')),
]

STREAMFIELD_ACADEMY_BLOCKS = [
    ('heading', blocks.CharBlock(classname="full title", icon="title")),
    ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
    ('image', ImageChooserBlock(icon="image")),
    ('aligned_image', AlignedImageBlock(icon="image")),
    ('video', EmbedBlock(icon="media")),
    ('Raw_HTML', HTMLBlock())
]

# Academy index page

class AcademyIndexPage(Page):
    subpage_types = ['academy.AcademyPage']

    class Meta:
        verbose_name = 'Academy Index Page'

    subtitle_de = models.CharField(
        max_length=250, blank=True, verbose_name="Title")
    subtitle_en = models.CharField(
        max_length=250, blank=True, verbose_name="Title")

    subtitle = TranslatedField(
        'subtitle_de',
        'subtitle_en'
    )

    @property
    def academy_pages(self):
        academy_pages = AcademyPage.objects.live()
        return academy_pages

    def get_context(self, request):
        academy_pages = self.academy_pages

        category = request.GET.get('category')

        if category:
            try:
                academy_pages = academy_pages.filter(category=category)
            except ValueError:
                academy_pages = []

        context = super().get_context(request)
        context['academy_pages'] = academy_pages
        context['topic'] = TOPIC_CHOICES
        if topic:
            context['current_topic'] = category
            for category_topic in TOPIC_CHOICES:
                if category_topic[0] == category:
                    context['get_current_topic_display'] = (
                        topic_choice[1]
                    )
        return context

    de_content_panels = [
        FieldPanel('subtitle_de'),
    ]

    en_content_panels = [
        FieldPanel('subtitle_en'),
    ]

    common_panels = [
        FieldPanel('title'),
        FieldPanel('slug'),
        # PageChooserPanel('form_page'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(common_panels, heading='Common'),
        ObjectList(en_content_panels, heading='English'),
        ObjectList(de_content_panels, heading='German')
    ])

    class Meta:
        verbose_name = 'Academy Index Page'

# Academy detail page

class AcademyPage(BlogPage):

    category = models.CharField(
        max_length=2,
        choices=TOPIC_CHOICES
    )

    class Meta:
        verbose_name = 'Academy Page'

    def get_context(self, request):
        topic = self.topic

        if topic:
            try:
                academy = AcademyPage.objects\
                    .filter(topic=topic)\
                    .exclude(id=self.id)
            except ValueError:
                academy = []

        context = super().get_context(request)
        context['academy'] = academy
        return context
