from django import forms
from django.core.paginator import Paginator, InvalidPage
from django.db.models import Count
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.db import models
from multiselectfield import MultiSelectField
from wagtail.admin.edit_handlers import (FieldPanel, MultiFieldPanel,
                                                ObjectList, StreamFieldPanel,
                                                TabbedInterface)
from wagtail.core.models import Page
from apps.blog.models import AbstractBlogPage
from apps.core.models.abstract_page_model import TranslatedStreamFieldPage

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


class AcademyOverviewPage(TranslatedStreamFieldPage):
    subpage_types = ['academy.AcademyPage']

    @property
    def years(self):
        return AcademyPage.objects.extra(
            select={'year': "strftime('%%Y',date)"}).values(
            'year').order_by().annotate(Count('id'))

    @property
    def topics(self):
        return TOPIC_CHOICES

    @property
    def academy_pages(self):
        academy_pages = AcademyPage.objects.live().descendant_of(self)
        academy_pages = academy_pages.order_by('-date')
        return academy_pages

    def get_context(self, request):
        academy_pages = self.academy_pages

        year = request.GET.get('year')
        topic = request.GET.get('topic')

        if year:
            academy_pages = academy_pages.filter(date__year=year)

        if topic:
            academy_pages = academy_pages.filter(topics__contains=topic)

        page = request.GET.get('page', 1)
        paginator = Paginator(academy_pages, 6)

        try:
            academy_pages = paginator.page(page)
        except InvalidPage:
            raise Http404

        context = super().get_context(request)
        context['academy_pages'] = academy_pages
        if topic:
            context['topic'] = topic
        if year:
            context['year'] = year
        return context

    def serve(self, request):
        context = self.get_context(request)
        academy_pages = context['academy_pages']

        if request.is_ajax():
            html = render_to_string(
                'academy/ajax/academy_list.html',
                {'request': request, 'academy_pages': academy_pages.object_list})
            return HttpResponse(html)
        return render(request,
                      self.template, context)

    class Meta:
        verbose_name = 'Academy Overview Page'
