from django import forms
from django.core.paginator import InvalidPage, Paginator
from django.db import models
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from modelcluster.fields import ParentalManyToManyField
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, MultiFieldPanel,
                                                ObjectList, StreamFieldPanel,
                                                TabbedInterface)
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wcag_contrast_ratio import contrast

from apps.core import blocks as core_blocks
from apps.core.models.abstract_page_model import TranslatedStreamFieldPage
from apps.core.models.snippets import ProjectCategory
from apps.persons import models as persons_models
from contrib.translations.translations import TranslatedField

STREAMFIELD_PROJECT_BLOCKS = [
    ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
    ('image', ImageChooserBlock(icon="image")),
    ('video', EmbedBlock(icon="media")),
    ('Raw_HTML', core_blocks.HTMLBlock()),
    ('persons', persons_models.PersonListBlock()),
]


class ProjectPage(Page):

    class Meta:
        verbose_name = 'Project'

    subpage_types = []

    # translateable fields
    title_en = models.CharField(
        max_length=255, verbose_name="Title")
    title_de = models.CharField(
        max_length=255, blank=True, verbose_name="Title")

    subtitle_de = models.CharField(
        max_length=255, default="", blank=True, verbose_name="Subtitle")
    subtitle_en = models.CharField(
        max_length=255, default="", blank=True, verbose_name="Subtitle")

    shorttext_de = RichTextField(
        max_length=300, blank=True, default="", verbose_name="Teasertext")
    shorttext_en = RichTextField(
        max_length=300, blank=True, default="", verbose_name="Teasertext")

    body_de = StreamField(
        STREAMFIELD_PROJECT_BLOCKS,
        null=True, blank=True, verbose_name="Body")
    body_en = StreamField(
        STREAMFIELD_PROJECT_BLOCKS,
        null=True, verbose_name="Body")

    body = TranslatedField(
        'body_de',
        'body_en'
    )

    translated_title = TranslatedField(
        'title_de',
        'title_en',
    )

    translated_subtitle = TranslatedField(
        'subtitle_de',
        'subtitle_en',
    )

    translated_shorttext = TranslatedField(
        'shorttext_de',
        'shorttext_en',
    )

    translated_external_url = TranslatedField(
        'external_url_de',
        'external_url_en',
    )

    # common fields

    image = models.ForeignKey(
        'images.CustomImage',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='+'
    )

    color1 = models.CharField(max_length=7, default='#d9b058')
    color2 = models.CharField(max_length=7, default='#a37146')

    external_url = models.URLField(max_length=200, blank=True)
    categories = ParentalManyToManyField('core.ProjectCategory', blank=True)
    timescale = models.CharField(max_length=256, blank=True)
    partner = models.CharField(max_length=256, blank=True)
    user_count = models.CharField(max_length=256,
                                  blank=True,
                                  verbose_name='Number of users per month')

    de_content_panels = [
        FieldPanel('title_de'),
        FieldPanel('subtitle_de'),
        FieldPanel('shorttext_de'),
        StreamFieldPanel('body_de')
    ]

    en_content_panels = [
        FieldPanel('title_en'),
        FieldPanel('subtitle_en'),
        FieldPanel('shorttext_en'),
        StreamFieldPanel('body_en')
    ]

    appearance_panels = [
        ImageChooserPanel('image'),
        FieldPanel('color1'),
        FieldPanel('color2')
    ]

    statistics_panels = [
        FieldPanel('external_url'),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        FieldPanel('timescale'),
        FieldPanel('partner'),
        FieldPanel('user_count')
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
        ObjectList(appearance_panels, heading='Appearance'),
        ObjectList(statistics_panels, heading='Statistics'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(
            Page.settings_panels, heading='Settings', classname="settings"),
    ])

    subpage_types = []

    @staticmethod
    def _color_to_rgb(value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(
            int(value[i:i + lv // 3], 16)/255 for i in range(0, lv, lv // 3))

    @property
    def textcolor(self):
        rgb_1 = self._color_to_rgb(self.color1)
        rgb_2 = self._color_to_rgb(self.color2)
        # check the darker color of both gradient points
        rgb_to_check = rgb_1 if sum(rgb_1) < sum(rgb_2) else rgb_2

        contrast_dark = contrast.rgb(
            rgb_to_check,
            self._color_to_rgb('#060606')
        )
        contrast_bright = contrast.rgb(
            rgb_to_check,
            self._color_to_rgb('#fbfbfb')
        )
        return '#fbfbfb' if contrast_bright > contrast_dark else '#060606'


class ProjectIndexPage(TranslatedStreamFieldPage):

    subpage_types = ['projects.ProjectPage']

    class Meta:
        verbose_name = 'Project List'

    @property
    def projects(self):
        projects = ProjectPage.objects.all().live()
        projects = projects.order_by('title')
        return projects

    def get_context(self, request):
        projects = self.projects

        category = request.GET.get('category')

        if category:
            projects = projects.filter(categories__pk=category)

        page = request.GET.get('page', 1)
        paginator = Paginator(projects, 6)

        try:
            projects = paginator.page(page)
        except InvalidPage:
            raise Http404

        context = super().get_context(request)
        context['projects'] = projects
        context['categories'] = ProjectCategory.objects.all()
        if category:
            context['category'] = ProjectCategory.objects.get(pk=int(category))
        return context

    def serve(self, request):
        context = self.get_context(request)
        categories = context['categories']
        projects = context['projects']
        category = None
        if 'category' in context:
            category = context['category']

        if request.is_ajax():
            html = render_to_string(
                'projects/project_list.html',
                {'request': request, 'projects': projects.object_list})
            return HttpResponse(html)
        return render(request,
                      self.template, {'projects': projects,
                                      'category': category,
                                      'categories': categories, 'self': self})
