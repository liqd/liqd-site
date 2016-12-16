from django.db import models
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from modelcluster.fields import ParentalKey
from taggit.models import Tag, TaggedItemBase
from modelcluster.tags import ClusterTaggableManager
from wagtail.wagtailsearch import index
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailadmin.edit_handlers import InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import TabbedInterface, ObjectList, MultiFieldPanel
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from core.models import TranslatedStreamFieldPage
from core.blocks import HTMLBlock
from contrib.translations.translations import TranslatedField



STREAMFIELD_BLOG_BLOCKS = [
    ('heading', blocks.CharBlock(classname="full title", icon="title")),
    ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
    ('image', ImageChooserBlock(icon="image")),
    ('video', EmbedBlock(icon="media")),
    ('Raw_HTML', HTMLBlock()),
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

    subtitle_en = models.CharField(max_length=255, default="", verbose_name="Subtitle")
    subtitle_de = models.CharField(max_length=255, default="", blank=True, verbose_name="Subtitle")

    intro_en = RichTextField(verbose_name="Teasertext")
    intro_de = RichTextField(blank=True, verbose_name="Teasertext")

    body_en = StreamField(STREAMFIELD_BLOG_BLOCKS, null=True, verbose_name="Body")
    body_de = StreamField(STREAMFIELD_BLOG_BLOCKS, null=True, blank=True, verbose_name="Body")

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
        ObjectList(common_panels, heading='Author and Date'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(
            Page.settings_panels, heading='Settings', classname="settings"),
    ])

# Blog index page
class BlogIndexPage(TranslatedStreamFieldPage):
    subpage_types = ['blog.BlogPage']

    @property
    def blogs(self):
        blogs = BlogPage.objects.live().descendant_of(self)
        blogs = blogs.order_by('-date')
        return blogs

    def get_context(self, request):
        blogs = self.blogs
        page = request.GET.get('page')
        paginator = Paginator(blogs, 5)
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

        context = super(BlogIndexPage, self).get_context(request)
        context['blogs'] = blogs
        return context

    def serve(self, request):
        blogs = self.get_context(request)['blogs']
        if request.is_ajax():
            html = render_to_string(
                'blog/ajax/blog_list.html', {'request': request, 'blogs': blogs.object_list})
            return HttpResponse(html)
        return render(request, self.template, {'blogs': blogs, 'self': self})

    class Meta:
        verbose_name = 'Blog Index Page'
