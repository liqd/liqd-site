import random

from django import forms
from django.core.paginator import InvalidPage
from django.core.paginator import Paginator
from django.db import models
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.functional import cached_property
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

from apps.core import blocks as core_blocks
from apps.core.models.abstract_page_model import TranslatedStreamFieldPage
from apps.core.models.snippets import ProjectCategory
from apps.persons import models as persons_models
from contrib.translations.translations import TranslatedField

STREAMFIELD_PROJECT_BLOCKS = [
    ("paragraph", blocks.RichTextBlock(icon="pilcrow")),
    (
        "image",
        ImageChooserBlock(icon="image", template="blocks/block_image.html"),
    ),
    ("aligned_image", core_blocks.AlignedImageBlock(icon="image")),
    ("Raw_HTML", core_blocks.HTMLBlock()),
    ("persons", persons_models.PersonListBlock()),
    ("video_block", core_blocks.VideoBlock()),
]


class ProjectPage(Page):
    class Meta:
        verbose_name = "Project"

    subpage_types = []

    # translateable fields
    title_en = models.CharField(
        max_length=255, blank=True, verbose_name="Title"
    )
    title_de = models.CharField(
        max_length=255, blank=True, verbose_name="Title"
    )

    subtitle_de = models.CharField(
        max_length=255, default="", blank=True, verbose_name="Subtitle"
    )
    subtitle_en = models.CharField(
        max_length=255, default="", blank=True, verbose_name="Subtitle"
    )

    shorttext_de = RichTextField(
        max_length=300, blank=True, default="", verbose_name="Teasertext"
    )
    shorttext_en = RichTextField(
        max_length=300, blank=True, default="", verbose_name="Teasertext"
    )

    body_de = StreamField(
        STREAMFIELD_PROJECT_BLOCKS,
        null=True,
        blank=True,
        verbose_name="Body",
        use_json_field=True,
    )
    body_en = StreamField(
        STREAMFIELD_PROJECT_BLOCKS,
        null=True,
        blank=True,
        verbose_name="Body",
        use_json_field=True,
    )

    timescale_en = models.CharField(max_length=256, blank=True)
    timescale_de = models.CharField(max_length=256, blank=True)

    partner_en = models.CharField(max_length=256, blank=True)
    partner_de = models.CharField(max_length=256, blank=True)

    user_count_en = models.CharField(
        max_length=256, blank=True, verbose_name="Number of users per month"
    )
    user_count_de = models.CharField(
        max_length=256, blank=True, verbose_name="Number of users per month"
    )

    timescale = TranslatedField("timescale_de", "timescale_en")
    partner = TranslatedField("partner_de", "partner_en")
    user_count = TranslatedField("user_count_de", "user_count_en")

    body = TranslatedField("body_de", "body_en")

    translated_title = TranslatedField(
        "title_de",
        "title_en",
    )

    translated_subtitle = TranslatedField(
        "subtitle_de",
        "subtitle_en",
    )

    translated_shorttext = TranslatedField(
        "shorttext_de",
        "shorttext_en",
    )

    translated_external_url = TranslatedField(
        "external_url_de",
        "external_url_en",
    )

    # common fields

    image = models.ForeignKey(
        "images.CustomImage",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="+",
    )

    color1 = models.CharField(max_length=7, default="#d9b058")
    color2 = models.CharField(max_length=7, default="#a37146")

    external_url = models.URLField(max_length=200, blank=True)
    categories = ParentalManyToManyField("core.ProjectCategory", blank=True)

    de_content_panels = [
        FieldPanel("title_de"),
        FieldPanel("subtitle_de"),
        FieldPanel("shorttext_de"),
        FieldPanel("timescale_de"),
        FieldPanel("partner_de"),
        FieldPanel("user_count_de"),
        FieldPanel("body_de"),
    ]

    en_content_panels = [
        FieldPanel("title_en"),
        FieldPanel("subtitle_en"),
        FieldPanel("shorttext_en"),
        FieldPanel("timescale_en"),
        FieldPanel("partner_en"),
        FieldPanel("user_count_en"),
        FieldPanel("body_en"),
    ]

    appearance_panels = [
        FieldPanel("image"),
        FieldPanel("color1"),
        FieldPanel("color2"),
    ]

    commons_panels = [
        FieldPanel("external_url"),
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
            heading="SEO settings",
            classname="collapsible",
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(en_content_panels, heading="English"),
            ObjectList(de_content_panels, heading="German"),
            ObjectList(appearance_panels, heading="Appearance"),
            ObjectList(commons_panels, heading="Common"),
            ObjectList(promote_panels, heading="Promote"),
            ObjectList(
                Page.settings_panels, heading="Settings", classname="settings"
            ),
        ]
    )

    subpage_types = []

    @cached_property
    def other_project(self):
        category_list = self.categories.all().values_list("pk", flat=True)
        if category_list:
            return random.choice(
                ProjectPage.objects.filter(categories__in=category_list)
                .live()
                .exclude(pk=self.pk)
            )


class ProjectIndexPage(TranslatedStreamFieldPage):
    subpage_types = ["projects.ProjectPage"]

    class Meta:
        verbose_name = "Project List"

    @property
    def projects(self):
        projects = ProjectPage.objects.all().live()
        projects = projects.order_by("title")
        return projects

    def get_context(self, request):
        projects = self.projects

        category = request.GET.get("category")

        if category:
            projects = projects.filter(categories__pk=category)

        page = request.GET.get("page", 1)
        paginator = Paginator(projects, 6)

        try:
            projects = paginator.page(page)
        except InvalidPage:
            raise Http404

        context = super().get_context(request)
        context["page_number"] = paginator.num_pages
        context["projects"] = projects
        context["categories"] = ProjectCategory.objects.all()
        if category:
            context["category"] = ProjectCategory.objects.get(pk=int(category))
        return context

    def serve(self, request):
        context = self.get_context(request)
        categories = context["categories"]
        projects = context["projects"]
        page_number = context["page_number"]
        category = None
        if "category" in context:
            category = context["category"]

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            html = render_to_string(
                "projects/project_list.html",
                {"request": request, "projects": projects.object_list},
            )
            return HttpResponse(html)
        return render(
            request,
            self.template,
            {
                "projects": projects,
                "category": category,
                "page_number": page_number,
                "categories": categories,
                "self": self,
            },
        )
