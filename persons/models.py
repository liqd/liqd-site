from django.db import models
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore import blocks as core_blocks
from wagtail.wagtailsnippets import blocks as snippet_blocks
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel
from wagtail.wagtailadmin.edit_handlers import InlinePanel
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from wagtail.wagtailadmin.edit_handlers import TabbedInterface, ObjectList

from contrib.translations.translations import TranslatedField


VORSTAND = 'Vorstand'
PROJEKTMANAGEMENT = 'Projektmanagement'
ENTWICKLUNG = 'Entwicklung'
DESIGN = 'Design'

AREAS_CHOICES = (
    (VORSTAND, 'Vorstand'),
    (PROJEKTMANAGEMENT, 'Projektmanagement'),
    (ENTWICKLUNG, 'Entwicklung'),
    (DESIGN, 'Design'),
)


class ContactFields(models.Model):
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    panels = [
        FieldPanel('telephone'),
        FieldPanel('email')
    ]

    class Meta:
        abstract = True

# Person page


class PersonPage(Page, ContactFields):
    parent_page_types = ['persons.PersonIndexPage']
    subpage_types = []
@register_snippet
class PersonSnippet(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    biography = RichTextField(blank=True)
    area = models.CharField(max_length=256, choices=AREAS_CHOICES)
    email = models.EmailField(blank=True)

    motto_de = RichTextField(blank=True)
    motto_en = RichTextField(blank=True)

    area_de = models.CharField(max_length=256)
    area_en = models.CharField(max_length=256)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    @property
    def persons(self):
        persons = PersonPage.objects.live()
        persons = persons.order_by('last_name')
        return persons

    def serve(self, request):
        blogpages = self.blogpages
        persons = self.persons
        area = request.GET.getlist('area')

        if area:
            persons = persons.filter(area__in=area)

        if request.is_ajax():
            html = render_to_string(
                'persons/includes/person_list.html', {'request': request, 'persons': persons})
            return HttpResponse(html)

        return render(request, self.template, {
            'self': self,
            'persons': persons,
            'choices': [choice[0] for choice in AREAS_CHOICES],
            'title': (list(self.get_ancestors()))[-1].title,
            'blogpages': blogpages
        })

    search_fields = Page.search_fields + (
        index.SearchField('first_name'),
        index.SearchField('last_name'),
        index.SearchField('intro'),
        index.SearchField('biography'),
    area = TranslatedField(
        'area_de',
        'area_en'
    )

PersonPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('first_name'),
    FieldPanel('last_name'),
    FieldPanel('biography', classname="full"),
    FieldPanel('area', classname="full"),
    ImageChooserPanel('image'),
    MultiFieldPanel(ContactFields.panels, "Contact")
]

PersonPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
]


class PersonIndexPage(Page):
    intro = RichTextField(blank=True)
    subpage_types = ['persons.PersonPage']

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
    motto = TranslatedField(
        'motto_de',
        'motto_en'
    )

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def persons(self):
        persons = PersonPage.objects.live()
        persons = persons.order_by('last_name')
        return persons

    def serve(self, request):
        persons = self.persons
        area = request.GET.getlist('area')

        if area:
            persons = persons.filter(area__in=area)

        if request.is_ajax():
            html = render_to_string(
                'persons/includes/person_list.html', {'request': request, 'persons': persons})
            return HttpResponse(html)

        return render(request, self.template, {
            'self': self,
            'persons': persons,
            'choices': [choice[0] for choice in AREAS_CHOICES]
        })

PersonIndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full")
]

PersonIndexPage.promote_panels = Page.promote_panels
