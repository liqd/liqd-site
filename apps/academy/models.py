import operator
from functools import reduce
from itertools import chain

from django import forms
from django.core.paginator import InvalidPage
from django.core.paginator import Paginator
from django.db import models
from django.db.models import Q
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import MultiFieldPanel
from wagtail.admin.panels import ObjectList
from wagtail.admin.panels import PageChooserPanel
from wagtail.admin.panels import TabbedInterface
from wagtail.admin.panels.title_field_panel import TitleFieldPanel
from wagtail.admin.widgets.slug import SlugInput
from wagtail.fields import RichTextField
from wagtail.fields import StreamField
from wagtail.models import Page

from apps.academy.blocks import AcademyCallToActionBlock
from apps.academy.blocks import AcademySingleTeaserBlock
from apps.academy.blocks import AcademyTeaserColumnsListBlock
from apps.academy.blocks import ChallengeStepBlock
from apps.academy.blocks import TopicBlockList
from apps.academy.choices import TOPIC_CHOICES
from apps.blog.models import AbstractBlogPage
from contrib.translations.translations import TranslatedField

WORKSHOP = "WS"
ARTICLE = "AR"
VIDEO = "VD"
LINKLIST = "LL"

CONTENT_TYPE_CHOICES = [
    (WORKSHOP, _("workshop")),
    (ARTICLE, _("article")),
    (VIDEO, _("video")),
    (LINKLIST, _("link collection")),
]

STREAMFIELD_CHALLENGE_BLOCKS = [("challenge_tasks", ChallengeStepBlock())]

STREAMFIELD_LP_BLOCKS = [
    ("single_teaser", AcademySingleTeaserBlock()),
    ("call_to_action_teaser", AcademyCallToActionBlock()),
    ("topic_block_list", TopicBlockList()),
    ("teaser_columns", AcademyTeaserColumnsListBlock()),
]

STREAMFIELD_EXTRA_BLOCKS = [
    ("call_to_action_teaser", AcademyCallToActionBlock())
]


class AcademyPage(AbstractBlogPage):
    topics = MultiSelectField(
        max_length=8, max_choices=3, choices=TOPIC_CHOICES
    )

    academy_content_type = models.CharField(
        max_length=2, choices=CONTENT_TYPE_CHOICES, blank=True
    )

    tile_image = models.ForeignKey(
        "images.CustomImage",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="+",
        help_text="The image used for the tile teaser",
    )

    class Meta:
        verbose_name = "Academy Page"

    teaser_en = StreamField(
        STREAMFIELD_EXTRA_BLOCKS,
        null=True,
        blank=True,
        verbose_name="Teaser",
        use_json_field=True,
    )
    teaser_de = StreamField(
        STREAMFIELD_EXTRA_BLOCKS,
        null=True,
        blank=True,
        verbose_name="Teaser",
        use_json_field=True,
    )
    teaser = TranslatedField("teaser_de", "teaser_en")

    en_content_panels = [
        FieldPanel("title_en"),
        FieldPanel("subtitle_en"),
        FieldPanel("intro_en"),
        FieldPanel("body_en"),
        FieldPanel("teaser_en"),
    ]

    de_content_panels = [
        FieldPanel("title_de"),
        FieldPanel("subtitle_de"),
        FieldPanel("intro_de"),
        FieldPanel("body_de"),
        FieldPanel("teaser_de"),
    ]

    common_panels = [
        FieldPanel("author"),
        FieldPanel("date"),
        FieldPanel("topics", widget=forms.CheckboxSelectMultiple),
        FieldPanel("academy_content_type"),
        FieldPanel("tile_image"),
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
        ]
    )

    def get_topic_related_content(self):
        topics = self.topics

        # construct query to find all content whose topic set
        # intersects with current topic set
        clauses = (Q(topics__contains=topic) for topic in topics)
        query = reduce(operator.or_, clauses)

        other_pages = AcademyPage.objects.filter(query).exclude(id=self.id)
        other_links = AcademyExternalLink.objects.filter(query).exclude(
            id=self.id
        )

        # first order by number of topic intersections, then by date
        other_content = sorted(
            chain(other_pages, other_links),
            key=operator.attrgetter("date"),
            reverse=True,
        )

        def get_sort_key(other_page):
            return len(set(topics) & set(other_page.topics))

        other_content = sorted(other_content, key=get_sort_key, reverse=True)
        return other_content

    def get_context(self, request):
        context = super().get_context(request)
        context["other_content"] = self.get_topic_related_content()[0:3]
        return context


class AcademyExternalLink(Page):
    # Translatable Fields
    title_en = models.CharField(
        max_length=255, blank=True, verbose_name="Title en"
    )
    title_de = models.CharField(
        max_length=255, blank=True, verbose_name="Title de"
    )
    translated_title = TranslatedField(
        "title_de",
        "title_en",
    )

    intro_en = RichTextField(blank=True, verbose_name="Teasertext")
    intro_de = RichTextField(blank=True, verbose_name="Teasertext")
    translated_intro = TranslatedField(
        "intro_de",
        "intro_en",
    )

    # common fields
    date = models.DateField("Post date")

    external_link = models.URLField(help_text="URL to an external website")

    topics = MultiSelectField(
        max_length=8, max_choices=3, choices=TOPIC_CHOICES
    )

    academy_content_type = models.CharField(
        max_length=2, choices=CONTENT_TYPE_CHOICES, blank=True
    )

    tile_image = models.ForeignKey(
        "images.CustomImage",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="+",
        help_text="The image used for the tile teaser",
    )

    en_content_panels = [
        FieldPanel("title_en"),
        FieldPanel("intro_en"),
    ]

    de_content_panels = [
        FieldPanel("title_de"),
        FieldPanel("intro_de"),
    ]

    common_panels = [
        FieldPanel("date"),
        FieldPanel("external_link"),
        FieldPanel("topics", widget=forms.CheckboxSelectMultiple),
        FieldPanel("academy_content_type"),
        FieldPanel("tile_image"),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(en_content_panels, heading="English"),
            ObjectList(de_content_panels, heading="German"),
            ObjectList(common_panels, heading="Common"),
        ]
    )

    preview_modes = []
    url = None

    def save(self, update_fields=None, *args, **kwargs):
        self.slug = self.id
        self.title = self.title_en
        if update_fields:
            update_fields = {"slug", "title"}.union(update_fields)
        super().save(update_fields=update_fields, *args, **kwargs)


class AcademyChallengePage(Page):
    tile_image = models.ForeignKey(
        "images.CustomImage",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="+",
        help_text="The image used for the tile teaser",
    )

    title_en = models.CharField(
        max_length=255, blank=True, verbose_name="Title"
    )
    title_de = models.CharField(
        max_length=255, blank=True, verbose_name="Title"
    )
    translated_title = TranslatedField(
        "title_de",
        "title_en",
    )

    subtitle_en = models.CharField(
        max_length=500, blank=True, verbose_name="Subtitle"
    )
    subtitle_de = models.CharField(
        max_length=500, blank=True, verbose_name="Subtitle"
    )
    translated_subtitle = TranslatedField(
        "subtitle_de",
        "subtitle_en",
    )

    completion_time_en = models.CharField(
        max_length=500, blank=True, verbose_name="Time to complete"
    )
    completion_time_de = models.CharField(
        max_length=500, blank=True, verbose_name="Time to complete"
    )
    translated_completion_time = TranslatedField(
        "completion_time_de",
        "completion_time_en",
    )

    intro_en = RichTextField(blank=True, verbose_name="Teaser text")
    intro_de = RichTextField(blank=True, verbose_name="Teaser text")
    translated_intro = TranslatedField(
        "intro_de",
        "intro_en",
    )

    body_en = StreamField(
        STREAMFIELD_CHALLENGE_BLOCKS,
        null=True,
        blank=True,
        verbose_name="Challenge step",
        use_json_field=True,
        min_num=2,
        max_num=5,
    )
    body_de = StreamField(
        STREAMFIELD_CHALLENGE_BLOCKS,
        null=True,
        blank=True,
        verbose_name="Challenge step",
        use_json_field=True,
        max_num=5,
    )
    body = TranslatedField("body_de", "body_en")

    teaser_en = StreamField(
        STREAMFIELD_EXTRA_BLOCKS,
        null=True,
        blank=True,
        verbose_name="Teaser",
        use_json_field=True,
    )
    teaser_de = StreamField(
        STREAMFIELD_EXTRA_BLOCKS,
        null=True,
        blank=True,
        verbose_name="Teaser",
        use_json_field=True,
    )
    teaser = TranslatedField("teaser_de", "teaser_en")

    en_content_panels = [
        FieldPanel("title_en"),
        FieldPanel("subtitle_en"),
        FieldPanel("completion_time_en"),
        FieldPanel("intro_en"),
        FieldPanel("body_en"),
        FieldPanel("teaser_en"),
    ]

    de_content_panels = [
        FieldPanel("title_de"),
        FieldPanel("subtitle_de"),
        FieldPanel("completion_time_de"),
        FieldPanel("intro_de"),
        FieldPanel("body_de"),
        FieldPanel("teaser_de"),
    ]

    common_panels = [
        FieldPanel("tile_image"),
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
            ObjectList(common_panels, heading="Common"),
            ObjectList(promote_panels, heading="Promote"),
        ]
    )

    class Meta:
        verbose_name = "Academy Challenge"


class AcademyIndexPage(Page):
    subpage_types = ["academy.AcademyPage", "academy.AcademyExternalLink"]

    title_en = models.CharField(
        max_length=255, blank=True, verbose_name="Title"
    )
    title_de = models.CharField(
        max_length=255, blank=True, verbose_name="Title"
    )
    translated_title = TranslatedField(
        "title_de",
        "title_en",
    )

    intro_en = RichTextField(blank=True, verbose_name="intro text")
    intro_de = RichTextField(blank=True, verbose_name="intro text")
    translated_intro = TranslatedField(
        "intro_de",
        "intro_en",
    )

    body_en = StreamField(
        STREAMFIELD_EXTRA_BLOCKS,
        null=True,
        blank=True,
        verbose_name="Body",
        use_json_field=True,
    )
    body_de = StreamField(
        STREAMFIELD_EXTRA_BLOCKS,
        null=True,
        blank=True,
        verbose_name="Body",
        use_json_field=True,
    )
    body = TranslatedField("body_de", "body_en")

    en_content_panels = [
        FieldPanel("title_en"),
        FieldPanel("intro_en"),
        FieldPanel("body_en"),
    ]

    de_content_panels = [
        FieldPanel("title_de"),
        FieldPanel("intro_de"),
        FieldPanel("body_de"),
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
            ObjectList(promote_panels, heading="Promote"),
        ]
    )

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

    def get_context(self, request):
        academy_pages = self.academy_pages
        external_links = self.external_links

        year = request.GET.get("year")
        alphabetical = request.GET.get("alphabetical")
        topic = request.GET.get("topic")
        content_type = request.GET.get("academy_content_type")
        if year and year.isdigit() and int(year) <= 9999:
            academy_pages = academy_pages.filter(date__year=year)
            external_links = external_links.filter(date__year=year)

        if topic and topic in dict(TOPIC_CHOICES):
            academy_pages = academy_pages.filter(topics__contains=topic)
            external_links = external_links.filter(topics__contains=topic)

        if content_type and content_type in dict(CONTENT_TYPE_CHOICES):
            academy_pages = academy_pages.filter(
                academy_content_type=content_type
            )
            external_links = external_links.filter(
                academy_content_type=content_type
            )

        if alphabetical:
            all_content = sorted(
                chain(academy_pages, external_links),
                key=lambda title: operator.attrgetter("translated_title")(
                    title
                ).lower(),
            )

        else:
            all_content = sorted(
                chain(academy_pages, external_links),
                key=operator.attrgetter("date"),
                reverse=True,
            )

        page = request.GET.get("page", 1)
        paginator = Paginator(all_content, 9)

        try:
            all_content = paginator.page(page)
        except InvalidPage:
            raise Http404

        context = super().get_context(request)

        context["all_content"] = all_content
        if alphabetical:
            context["alphabetical"] = alphabetical
        if topic and topic in dict(TOPIC_CHOICES):
            context["topic"] = topic
            context["get_topic_display"] = self.topics[topic]
        if content_type and content_type in dict(CONTENT_TYPE_CHOICES):
            context["academy_content_type"] = content_type
            context["get_academy_content_type_display"] = (
                self.academy_content_types[content_type]
            )
        return context

    class Meta:
        verbose_name = "Academy Index Page"


class AcademyLandingPage(Page):
    subpage_types = [
        "academy.AcademyIndexPage",
        "academy.AcademyChallengePage",
    ]

    intro_text_en = models.CharField(
        max_length=255, verbose_name="intro text en", blank=True
    )
    intro_text_de = models.CharField(
        max_length=255, verbose_name="intro text de", blank=True
    )
    translated_intro_text = TranslatedField(
        "intro_text_de",
        "intro_text_en",
    )

    intro_link_text_en = models.CharField(
        max_length=100, verbose_name="intro link text en", blank=True
    )
    intro_link_text_de = models.CharField(
        max_length=100, verbose_name="intro link text de", blank=True
    )
    translated_intro_link_text = TranslatedField(
        "intro_link_text_de",
        "intro_link_text_en",
    )

    body_en = StreamField(
        STREAMFIELD_LP_BLOCKS,
        null=True,
        blank=True,
        verbose_name="Body",
        use_json_field=True,
    )
    body_de = StreamField(
        STREAMFIELD_LP_BLOCKS,
        null=True,
        blank=True,
        verbose_name="Body",
        use_json_field=True,
    )
    body = TranslatedField("body_de", "body_en")

    # common fields

    intro_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Choose the page the intro text links to",
    )

    color1 = models.CharField(max_length=7, default="#eee8aa")
    color2 = models.CharField(max_length=7, default="#e1bcbd")

    en_content_panels = [
        FieldPanel("intro_text_en"),
        FieldPanel("intro_link_text_en"),
        FieldPanel("body_en"),
    ]

    de_content_panels = [
        FieldPanel("intro_text_de"),
        FieldPanel("intro_link_text_de"),
        FieldPanel("body_de"),
    ]

    common_panels = [
        PageChooserPanel("intro_link"),
        FieldPanel("color1"),
        FieldPanel("color2"),
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
            ObjectList(common_panels, heading="Common"),
            ObjectList(promote_panels, heading="Promote"),
        ]
    )

    class Meta:
        verbose_name = "Academy Landing Page"
