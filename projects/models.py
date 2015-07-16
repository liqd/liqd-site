from django.db import models
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


class ProjectPage(Page):
    subtitle = models.CharField(max_length=255)
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )
    shorttext = RichTextField(max_length=300, blank=True)
    streamFieldTop = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('video', EmbedBlock(icon="media"))
    ], null=True)
    streamFieldBottom = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
    ], null=True)

ProjectPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('subtitle', classname="full title"),
    FieldPanel('shorttext', classname="full"),
    ImageChooserPanel('image'),
    StreamFieldPanel('streamFieldTop'),
    InlinePanel(ProjectPage, 'projects_persons', label="Staff"),
    StreamFieldPanel('streamFieldBottom')
]


class ProjectIndexPage(Page):
    intro = RichTextField(blank=True)
    subpage_types = ['projects.ProjectPage']

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
    )

    @property
    def projects(self):
        projects = ProjectPage.objects.all()
        projects = projects.order_by('title')
        return projects

ProjectIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full")
]
