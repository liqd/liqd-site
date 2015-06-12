from django.db import models
from django.shortcuts import render
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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Paragraph


class Paragraph(models.Model):
    title = models.CharField(max_length=255, help_text="Title")
    body = RichTextField(blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('body'),
    ]

    class Meta:
        abstract = True

# Blog page


class BlogParagraph(Orderable, Paragraph):
    page = ParentalKey('blog.BlogPage', related_name='paragraphs')


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('blog.BlogPage', related_name='tagged_items')


class BlogPage(Page):
    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []
    body = RichTextField()
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(
        PersonPage, blank=True, null=True, related_name='blogpages', on_delete=models.SET_NULL)
    author_string = models.CharField(max_length=255, blank=True, null=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    date = models.DateField("Post date")
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + (
        index.SearchField('body'),
    )

    @property
    def blog_index(self):
        # Find closest ancestor which is a blog index
        return self.get_ancestors().type(BlogIndexPage).last()

AUTHORS = [
    FieldPanel('author'),
    FieldPanel('author_string'),
]

BlogPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('subtitle', classname="full title"),
    FieldPanel('date'),
    MultiFieldPanel(
        AUTHORS,
        heading="Authors"
    ),
    FieldPanel('body', classname="full"),
    InlinePanel(BlogPage, 'paragraphs', label="Paragraphs")
]

BlogPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
    FieldPanel('tags'),
]


# Blog index page
class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    subpage_types = ['blog.BlogPage']

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
    )

    @property
    def blogs(self):
        blogs = BlogPage.objects.live().descendant_of(self)
        blogs = blogs.order_by('-date')
        return blogs

    def get_context(self, request):
        blogs = self.blogs

        tag = request.GET.get('tag')
        if tag:
            blogs = blogs.filter(tags__name=tag)

        page = request.GET.get('page')
        paginator = Paginator(blogs, 10)
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

BlogIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full")
]

BlogIndexPage.promote_panels = Page.promote_panels
