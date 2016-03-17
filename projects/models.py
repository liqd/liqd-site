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
    
    subtitle_de = models.CharField(max_length=255)
    subtitle_en = models.CharField(max_length=255)

    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )

    shorttext_de = RichTextField(max_length=300, blank=True)
    shorttext_en = RichTextField(max_length=300, blank=True)

    external_url_de = models.URLField(max_length=200, blank=True)
    external_url_en = models.URLField(max_length=200, blank=True)

    streamFieldTop_de = StreamField(STREAMFIELD_PROJECT_BLOCKS, null=True)
    streamFieldTop_en = StreamField(STREAMFIELD_PROJECT_BLOCKS, null=True, blank=True)

    streamFieldBottom_de =StreamField(STREAMFIELD_PROJECT_BLOCKS, null=True)
    streamFieldBottom_en =StreamField(STREAMFIELD_PROJECT_BLOCKS, null=True)


ProjectPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('subtitle', classname="full title"),
    FieldPanel('shorttext', classname="full"),
    ImageChooserPanel('image'),
    StreamFieldPanel('streamFieldTop'),
    # InlinePanel(ProjectPage, 'projects_persons', label="Staff"),
    StreamFieldPanel('streamFieldBottom'),
    FieldPanel('external_url'),
]


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