from django.db import models
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from modelcluster.fields import ParentalKey
from taggit.models import Tag, TaggedItemBase
from persons.models import PersonPage
from modelcluster.tags import ClusterTaggableManager
from wagtail.wagtailsearch import index
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel
from wagtail.wagtailadmin.edit_handlers import InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import TabbedInterface, ObjectList, MultiFieldPanel
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from core.models import TranslatedStreamFieldPage
from contrib.translations.translations import TranslatedField


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


class BlogPage(TranslatedStreamFieldPage):

    class Meta:
        verbose_name = 'Blog Entry'

    subpage_types = []

    subtitle_en = models.CharField(max_length=255, default="", blank=True)
    subtitle_de = models.CharField(max_length=255, default="", blank=True)

    author = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField("Post date")

    translated_heading1 = TranslatedField(
        'subtitle_de',
        'subtitle_en',
    )

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
            FieldPanel('slug'),
            FieldPanel('title'),
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
        ObjectList(de_content_panels, heading='Content de'),
        ObjectList(en_content_panels, heading='Content en'),
        ObjectList(common_panels, heading='Author and Date'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(
            Page.settings_panels, heading='Settings', classname="settings"),
    ])
