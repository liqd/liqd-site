from django import forms
from django.core.paginator import InvalidPage
from django.core.paginator import Paginator
from django.db import models
from django.db.models import CharField
from django.db.models import Count
from django.db.models.functions import Cast
from django.db.models.functions import ExtractYear
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from modelcluster.fields import ParentalManyToManyField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import MultiFieldPanel
from wagtail.admin.panels import ObjectList
from wagtail.admin.panels import TabbedInterface
from wagtail.admin.panels.title_field_panel import TitleFieldPanel
from wagtail.admin.widgets.slug import SlugInput
from wagtail.fields import RichTextField
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page

from apps.core.blocks import AlignedImageBlock
from apps.core.blocks import HTMLBlock
from apps.core.blocks import VideoBlock
from apps.core.models.abstract_page_model import TranslatedStreamFieldPage
from apps.core.models.snippets import BlogCategory
from contrib.translations.translations import TranslatedField

STREAMFIELD_BLOG_BLOCKS = [
    ("heading", blocks.CharBlock(classname="full title", icon="title")),
    ("paragraph", blocks.RichTextBlock(icon="pilcrow")),
    (
        "image",
        ImageChooserBlock(icon="image", template="blocks/block_image.html"),
    ),
    ("aligned_image", AlignedImageBlock(icon="image")),
    ("Raw_HTML", HTMLBlock()),
    ("video_block", VideoBlock()),
]


class AbstractBlogPage(Page):
    class Meta:
        abstract = True

    subpage_types = []

    # Translatable Fields
    title_en = models.CharField(
        max_length=255, blank=True, verbose_name="Title"
    )
    title_de = models.CharField(
        max_length=255, blank=True, verbose_name="Title"
    )

    subtitle_en = models.CharField(
        max_length=255, default="", blank=True, verbose_name="Subtitle"
    )
    subtitle_de = models.CharField(
        max_length=255, default="", blank=True, verbose_name="Subtitle"
    )

    intro_en = RichTextField(blank=True, verbose_name="Teasertext")
    intro_de = RichTextField(blank=True, verbose_name="Teasertext")

    body_en = StreamField(
        STREAMFIELD_BLOG_BLOCKS,
        null=True,
        blank=True,
        verbose_name="Body",
        use_json_field=True,
    )
    body_de = StreamField(
        STREAMFIELD_BLOG_BLOCKS,
        null=True,
        blank=True,
        verbose_name="Body",
        use_json_field=True,
    )

    translated_title = TranslatedField(
        "title_de",
        "title_en",
    )

    translated_subtitle = TranslatedField(
        "subtitle_de",
        "subtitle_en",
    )

    translated_intro = TranslatedField(
        "intro_de",
        "intro_en",
    )

    body = TranslatedField("body_de", "body_en")

    # Common Fields

    author = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField("Post date")


class BlogPage(AbstractBlogPage):
    class Meta:
        verbose_name = "Blog Entry"

    categories = ParentalManyToManyField("core.BlogCategory", blank=True)

    en_content_panels = [
        FieldPanel("title_en"),
        FieldPanel("subtitle_en"),
        FieldPanel("intro_en"),
        FieldPanel("body_en"),
    ]

    de_content_panels = [
        FieldPanel("title_de"),
        FieldPanel("subtitle_de"),
        FieldPanel("intro_de"),
        FieldPanel("body_de"),
    ]

    common_panels = [
        FieldPanel("author"),
        FieldPanel("date"),
        FieldPanel("categories", widget=forms.CheckboxSelectMultiple),
    ]

    promote_panels = [
        MultiFieldPanel(
            [
                TitleFieldPanel("title"),
                FieldPanel("slug", widget=SlugInput),
            ],
            heading="Slug and CMS Page Name",
        ),
        MultiFieldPanel(
            [
                FieldPanel("seo_title"),
                FieldPanel("search_description"),
            ],
            heading="SEO settings de",
            classname="collapsible",
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(en_content_panels, heading="English"),
            ObjectList(de_content_panels, heading="German"),
            ObjectList(common_panels, heading="Common"),
            ObjectList(promote_panels, heading="Promote"),
            ObjectList(
                Page.settings_panels, heading="Settings", classname="settings"
            ),
        ]
    )


class BlogIndexPage(TranslatedStreamFieldPage):
    subpage_types = ["blog.BlogPage"]

    @property
    def years(self):
        return (
            BlogPage.objects.annotate(year_int=ExtractYear("date"))
            .annotate(year=Cast("year_int", output_field=CharField()))
            .values("year")
            .order_by("-year")
            .annotate(id__count=Count("id"))
        )

    @property
    def categories(self):
        return BlogCategory.objects.all()

    @property
    def blogs(self):
        blogs = BlogPage.objects.live().descendant_of(self)
        blogs = blogs.order_by("-date")
        return blogs

    def get_context(self, request):
        blogs = self.blogs

        year = request.GET.get("year")
        category = request.GET.get("category")
        category_pks = self.categories.values_list("id", flat=True)

        if year and year.isdigit() and int(year) <= 9999:
            blogs = blogs.filter(date__year=year)

        if category and category.isdigit() and int(category) in category_pks:
            blogs = blogs.filter(categories__pk=category)

        page = request.GET.get("page", 1)
        paginator = Paginator(blogs, 6)

        try:
            blogs = paginator.page(page)
        except InvalidPage:
            raise Http404

        context = super().get_context(request)
        context["blogs"] = blogs
        if category and category.isdigit() and int(category) in category_pks:
            context["category"] = BlogCategory.objects.get(pk=int(category))
        if year and year.isdigit() and int(year) <= 9999:
            context["year"] = year
        return context

    def serve(self, request):
        context = self.get_context(request)
        blogs = context["blogs"]

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            html = render_to_string(
                "blog/ajax/blog_list.html",
                {"request": request, "blogs": blogs.object_list},
            )
            return HttpResponse(html)
        return render(request, self.template, context)

    class Meta:
        verbose_name = "Blog Index Page"
