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


@register_snippet
class PersonSnippet(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
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

    area = TranslatedField(
        'area_de',
        'area_en'
    )

    motto = TranslatedField(
        'motto_de',
        'motto_en'
    )

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    base_information_panels = [
        FieldPanel('first_name'),
        FieldPanel('last_name'),
        FieldPanel('email'),
        ImageChooserPanel('image'),
    ]

    en_content_panels = [
        FieldPanel('motto_en'),
        FieldPanel('area_en'),
    ]

    de_content_panels = [
        FieldPanel('motto_de'),
        FieldPanel('area_de'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(base_information_panels, heading='Base Informations'),
        ObjectList(en_content_panels, heading='English'),
        ObjectList(de_content_panels, heading='German'),
    ])


class PersonDisplayBlock(core_blocks.StructBlock):
    person = snippet_blocks.SnippetChooserBlock(
        required=True, target_model=PersonSnippet)

    class Meta:
        template = 'persons/includes/person.html'


class PersonListBlock(core_blocks.StructBlock):
    title = core_blocks.CharBlock(classname="full title", required=False)
    background = core_blocks.ChoiceBlock(choices=[
        ('grey', 'grey'),
        ('white', 'white'),
    ])
    personlist = core_blocks.ListBlock(PersonDisplayBlock)

    class Meta:
        template = 'persons/person_list.html'
        icon = 'snippet'
        label = 'Person Import'
