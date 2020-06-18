import operator
from functools import reduce
from itertools import chain

from django.db.models import Q
from multiselectfield import MultiSelectField

from django import forms
from django.core.paginator import Paginator, InvalidPage
from django.db import models
from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from wagtail.admin.edit_handlers import (FieldPanel, MultiFieldPanel,
                                         ObjectList, StreamFieldPanel,
                                         TabbedInterface)
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from apps.blog.models import AbstractBlogPage
from contrib.translations.translations import TranslatedField

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

    academy_content_type = models.CharField(
        max_length=2,
        choices=CONTENT_TYPE_CHOICES,
        blank=True
    )

    tile_image = models.ForeignKey(
        'images.CustomImage',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='+',
        help_text='The image used for the tile teaser'
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
        FieldPanel('academy_content_type'),
        ImageChooserPanel('tile_image'),
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
    ])

    def get_topic_related_content(self):
        topics = self.topics

        # construct query to find all content whose topic set
        # intersects with current topic set
        clauses = (Q(topics__contains=topic) for topic in topics)
        query = reduce(operator.or_, clauses)

        other_pages = AcademyPage.objects.filter(query).exclude(id=self.id)
        other_links = AcademyExternalLink.objects.filter(query) \
            .exclude(id=self.id)
        other_content = sorted(chain(other_pages, other_links),
                               key=operator.attrgetter('date'), reverse=True)
        return other_content

    def get_context(self, request):

        context = super().get_context(request)
        context['other_content'] = self.get_topic_related_content()[0:3]
        return context


class AcademyExternalLink(Page):

    # Translatable Fields
    title_en = models.CharField(
        max_length=255, verbose_name="Title en")
    title_de = models.CharField(
        max_length=255, blank=True, verbose_name="Title dt")
    translated_title = TranslatedField(
        'title_de',
        'title_en',
    )

    intro_en = RichTextField(verbose_name="Teasertext")
    intro_de = RichTextField(blank=True, verbose_name="Teasertext")
    translated_intro = TranslatedField(
        'intro_de',
        'intro_en',
    )

    # common fields
    date = models.DateField("Post date")

    external_link = models.URLField(
        help_text='URL to an external website')

    topics = MultiSelectField(
        max_length=8,
        max_choices=3,
        choices=TOPIC_CHOICES
    )

    academy_content_type = models.CharField(
        max_length=2,
        choices=CONTENT_TYPE_CHOICES,
        blank=True
    )

    tile_image = models.ForeignKey(
        'images.CustomImage',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='+',
        help_text='The image used for the tile teaser'
    )

    en_content_panels = [
        FieldPanel('title_en'),
        FieldPanel('intro_en'),
    ]

    de_content_panels = [
        FieldPanel('title_de'),
        FieldPanel('intro_de'),
    ]

    common_panels = [
        FieldPanel('date'),
        FieldPanel('external_link'),
        FieldPanel('topics', widget=forms.CheckboxSelectMultiple),
        FieldPanel('academy_content_type'),
        ImageChooserPanel('tile_image'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(en_content_panels, heading='English'),
        ObjectList(de_content_panels, heading='German'),
        ObjectList(common_panels, heading='Common'),
    ])

    def save(self, *args, **kwargs):
        self.slug = self.id
        self.title = self.title_en
        super().save(*args, **kwargs)


class AcademyIndexPage(Page):
    subpage_types = ['academy.AcademyPage', 'academy.AcademyExternalLink']

    title_en = models.CharField(max_length=255, verbose_name="Title")
    title_de = models.CharField(
        max_length=255, blank=True, verbose_name="Title")
    translated_title = TranslatedField(
        'title_de',
        'title_en',
    )

    intro_en = RichTextField(verbose_name="intro text")
    intro_de = RichTextField(blank=True, verbose_name="intro text")
    translated_intro = TranslatedField(
        'intro_de',
        'intro_en',
    )

    en_content_panels = [
        FieldPanel('title_en'),
        FieldPanel('intro_en'),
    ]

    de_content_panels = [
        FieldPanel('title_de'),
        FieldPanel('intro_de'),
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
            heading="SEO settings",
            classname="collapsible"),
    ]

    edit_handler = TabbedInterface([
        ObjectList(en_content_panels, heading='English'),
        ObjectList(de_content_panels, heading='German'),
        ObjectList(promote_panels, heading='Promote'),
    ])

    @property
    def years(self):
        return self.all_content.extra(
            select={'year': "strftime('%%Y',date)"}).values(
            'year').order_by().annotate(models.Count('id'))

    @property
    def topics(self):
        return dict(TOPIC_CHOICES)

    @property
    def academy_content_types(self):
        return dict(CONTENT_TYPE_CHOICES)

    @property
    def academy_pages(self):
        academy_pages = AcademyPage.objects.live().descendant_of(self)

        return academy_pages

    @property
    def external_links(self):
        external_links = AcademyExternalLink.objects.live().descendant_of(self)

        return external_links

    @property
    def all_content(self):
        return sorted(
            chain(self.academy_pages, self.external_links),
            key=operator.attrgetter('date'), reverse=True)

    def get_context(self, request):
        all_content = self.all_content

        year = request.GET.get('year')
        topic = request.GET.get('topic')
        content_type = request.GET.get('content_type')

        if year:
            all_content = all_content.filter(date__year=year)

        if topic:
            all_content = all_content.filter(topics__contains=topic)

        if content_type:
            all_content = all_content.filter(
                academy_content_type=content_type)
        page = request.GET.get('page', 1)
        paginator = Paginator(all_content, 6)

        try:
            all_content = paginator.page(page)
        except InvalidPage:
            raise Http404

        context = super().get_context(request)
        context['all_content'] = all_content
        if year:
            context['year'] = year
        if topic:
            context['topic'] = topic
        if content_type:
            context['academy_content_type'] = content_type
        return context

    class Meta:
        verbose_name = 'Academy Index Page'
