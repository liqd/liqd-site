from django.db import models
# from core import models
from core.models import TranslatedStreamFieldPage
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailsearch import index
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock

from wagtail.wagtailadmin.edit_handlers import TabbedInterface, ObjectList, MultiFieldPanel
from core import blocks as core_blocks

from contrib.translations.translations import TranslatedField


STREAMFIELD_PROJECT_BLOCKS = [
    ('heading', blocks.CharBlock(classname="full title", icon="title")),
    ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
    ('image', ImageChooserBlock(icon="image")),
    ('video', EmbedBlock(icon="media")),
    ('Raw_HTML', core_blocks.HTMLBlock()),
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
        STREAMFIELD_PROJECT_BLOCKS, null=True, blank=True, verbose_name="Body")
    body_en = StreamField(
        STREAMFIELD_PROJECT_BLOCKS, null=True, verbose_name="Body")

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
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='+'
    )

    external_url = models.URLField(max_length=200, blank=True)

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

    common_panels = [
        ImageChooserPanel('image'),
        FieldPanel('external_url')
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
        ObjectList(common_panels, heading='Image and Url'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(
            Page.settings_panels, heading='Settings', classname="settings"),
    ])

    subpage_types = []


class ProjectIndexPage(TranslatedStreamFieldPage):

    subpage_types = ['projects.ProjectPage']

    search_fields = Page.search_fields + (
        index.SearchField('intro_de'),
        index.SearchField('intro_en'),
    )

    class Meta:
        verbose_name = 'ProjectIndexPage'

    @property
    def projects(self):
        projects = ProjectPage.objects.all()
        projects = projects.order_by('title')
        return projects
