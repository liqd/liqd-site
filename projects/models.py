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


class Paragraph(models.Model):
    title = models.CharField(max_length=255, help_text="Title")
    body = RichTextField()
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )
    visible = models.BooleanField(default=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('body'),
        ImageChooserPanel('image'),
        FieldPanel('visible'),
    ]

    class Meta:
        abstract = True


class Person(models.Model):
    person = models.ForeignKey(
        PersonPage)

    panels = [
        FieldPanel('person')
    ]

    class Meta:
        abstract = True


class ProjectParagraphTop(Orderable, Paragraph):
    page = ParentalKey(
        'projects.ProjectPage', related_name='project_paragraphs_top')


class ProjectParagraphBottom(Orderable, Paragraph):
    page = ParentalKey(
        'projects.ProjectPage', related_name='project_paragraphs_bottom')


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

ProjectPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('subtitle', classname="full title"),
    FieldPanel('shorttext', classname="full"),
    ImageChooserPanel('image'),
    InlinePanel(ProjectPage, 'project_paragraphs_top', label="Paragraphs"),
    InlinePanel(ProjectPage, 'projects_persons', label="Staff"),
    InlinePanel(ProjectPage, 'project_paragraphs_bottom', label="Paragraphs")
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
