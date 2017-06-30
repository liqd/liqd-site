from django import forms
from django.core.paginator import InvalidPage, Paginator
from django.db import models
from django.db.models import Count
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

from apps.core.blocks import AlignedImageBlock, HTMLBlock
from apps.core.models.abstract_page_model import TranslatedStreamFieldPage
from apps.core.models.snippets import BlogCategory
from contrib.translations.translations import TranslatedField

STREAMFIELD_BLOG_BLOCKS = [
    ('heading', blocks.CharBlock(classname="full title", icon="title")),
    ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
    ('image', ImageChooserBlock(icon="image")),
    ('aligned_image', AlignedImageBlock(icon="image")),
    ('video', EmbedBlock(icon="media")),
    ('Raw_HTML', HTMLBlock())
]


class BlogPage(Page):

    class Meta:
        verbose_name = 'Blog Entry'

    subpage_types = []

    # Translatable Fields
    title_en = models.CharField(
        max_length=255, verbose_name="Title")
    title_de = models.CharField(
        max_length=255, blank=True, verbose_name="Title")

    subtitle_en = models.CharField(
        max_length=255, default="", verbose_name="Subtitle")
    subtitle_de = models.CharField(
        max_length=255, default="", blank=True, verbose_name="Subtitle")

    intro_en = RichTextField(verbose_name="Teasertext")
    intro_de = RichTextField(blank=True, verbose_name="Teasertext")

    body_en = StreamField(STREAMFIELD_BLOG_BLOCKS,
                          null=True, verbose_name="Body")
    body_de = StreamField(STREAMFIELD_BLOG_BLOCKS,
                          null=True, blank=True, verbose_name="Body")

    translated_title = TranslatedField(
        'title_de',
        'title_en',
    )

    translated_subtitle = TranslatedField(
        'subtitle_de',
        'subtitle_en',
    )

    translated_intro = TranslatedField(
        'intro_de',
        'intro_en',
    )

    body = TranslatedField(
        'body_de',
        'body_en'
    )

    # Common Fields

    author = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField("Post date")
    categories = ParentalManyToManyField('core.BlogCategory', blank=True)

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
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
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

# Blog index page


class BlogIndexPage(TranslatedStreamFieldPage):
    subpage_types = ['blog.BlogPage']

    @property
    def years(self):
        return BlogPage.objects.extra(
            select={'year': "strftime('%%Y',date)"}).values(
            'year').order_by().annotate(Count('id'))

    @property
    def categories(self):
        return BlogCategory.objects.all()

    @property
    def blogs(self):
        blogs = BlogPage.objects.live().descendant_of(self)
        blogs = blogs.order_by('-date')
        return blogs

    def get_context(self, request):
        blogs = self.blogs

        year = request.GET.get('year')
        category = request.GET.get('category')

        if year:
            blogs = blogs.filter(date__year=year)

        if category:
            blogs = blogs.filter(categories__pk=category)

        page = request.GET.get('page', 1)
        paginator = Paginator(blogs, 6)

        try:
            blogs = paginator.page(page)
        except InvalidPage:
            raise Http404

        context = super().get_context(request)
        context['blogs'] = blogs
        if category:
            print(BlogCategory.objects.get(pk=int(category)))
            context['category'] = BlogCategory.objects.get(pk=int(category))
        return context

    def serve(self, request):
        context = self.get_context(request)
        blogs = context['blogs']

        if request.is_ajax():
            html = render_to_string(
                'blog/ajax/blog_list.html',
                {'request': request, 'blogs': blogs.object_list})
            return HttpResponse(html)
        return render(request,
                      self.template, context)

    class Meta:
        verbose_name = 'Blog Index Page'
