from django.db import models
# from core import models
from core.models import TranslatedStreamFieldPage
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailsearch import index
from modelcluster.fields import ParentalKey
from persons.models import PersonPage
from wagtail.wagtailadmin.edit_handlers import InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock

from wagtail.wagtailadmin.edit_handlers import TabbedInterface, ObjectList, MultiFieldPanel

from contrib.translations.translations import TranslatedField

class Person(models.Model):
    person = models.ForeignKey(
        PersonPage)

    panels = [
        FieldPanel('person')
    ]

    class Meta:
        abstract = True


class ProjectPersons(Orderable, Person):
    page = ParentalKey(
        'projects.ProjectPage', related_name='projects_persons')


STREAMFIELD_PROJECT_BLOCKS = [
    ('heading', blocks.CharBlock(classname="full title", icon="title")),
    ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
    ('image', ImageChooserBlock(icon="image")),
    ('video', EmbedBlock(icon="media"))
]


class ProjectPage(Page):

    title_en = models.CharField(max_length=255, blank=True, verbose_name="Header Title")
    title_de = models.CharField(max_length=255, blank=True, verbose_name="Header Title")
    
    subtitle_de = models.CharField(max_length=255, default="")
    subtitle_en = models.CharField(max_length=255, default="")

    image_de = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )
    image_en= models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )

    shorttext_de = RichTextField(max_length=300, blank=True, default="")
    shorttext_en = RichTextField(max_length=300, blank=True, default="")

    external_url_de = models.URLField(max_length=200, blank=True)
    external_url_en = models.URLField(max_length=200, blank=True)

    streamFieldTop_de = StreamField(STREAMFIELD_PROJECT_BLOCKS, null=True)
    streamFieldTop_en = StreamField(STREAMFIELD_PROJECT_BLOCKS, null=True, blank=True)

    streamFieldBottom_de =StreamField(STREAMFIELD_PROJECT_BLOCKS, null=True)
    streamFieldBottom_en =StreamField(STREAMFIELD_PROJECT_BLOCKS, null=True)


    streamFieldTop = TranslatedField(
        'streamFieldTop_de',
        'streamFieldTop_en'
    )

    streamFieldTop = TranslatedField(
        'streamFieldBottom_de',
        'streamFieldBottom_en'
    )

    translated_title = TranslatedField(
        'title_de',
        'title_en',
    )

    translated_subtitle = TranslatedField(
        'subtitle_de',
        'subtitle_en',
    )

    translated_image = TranslatedField(
        'image_de',
        'image_en',
    )

    translated_shorttext = TranslatedField(
        'shorttext_de',
        'shorttext_en',
    )

    translated_external_url = TranslatedField(
        'external_url_de',
        'external_url_en',
    )

    de_content_panels = [
        FieldPanel('title_de'),
        FieldPanel('subtitle_de'),
        FieldPanel('shorttext_de'),
        StreamFieldPanel('streamFieldTop_de'),
        ImageChooserPanel('image_de'),
        StreamFieldPanel('streamFieldBottom_de'),
        FieldPanel('external_url_de'),
    ]

    en_content_panels = [
        FieldPanel('title_en'),
        FieldPanel('subtitle_en'),
        FieldPanel('shorttext_en'),
        StreamFieldPanel('streamFieldTop_en'),
        ImageChooserPanel('image_en'),
        StreamFieldPanel('streamFieldBottom_en'),
        FieldPanel('external_url_en'),
    ]

    promote_panels = [
        MultiFieldPanel([
            FieldPanel('slug'),
            FieldPanel('title'),
        ],
        heading = "Slug and CMS Page Name"),
        MultiFieldPanel([
            FieldPanel('seo_title'),
            FieldPanel('search_description'),
        ],
        heading = "SEO settings",
        classname="collapsible"),
    ]

    edit_handler = TabbedInterface([
        ObjectList(de_content_panels, heading='Content de'),
        ObjectList(en_content_panels, heading='Content en'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    ])

    subpage_types = []


class ProjectIndexPage(TranslatedStreamFieldPage):
    
    subpage_types = ['projects.ProjectPage']

    search_fields = Page.search_fields + (
        index.SearchField('intro_de'),
        index.SearchField('intro_en'),
    )

    @property
    def projects(self):
        projects = ProjectPage.objects.all()
        projects = projects.order_by('title')
        return projects