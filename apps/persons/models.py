from django.db import models
from wagtail.admin.panels import FieldPanel, ObjectList, TabbedInterface
from wagtail import blocks as core_blocks
from wagtail.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets import blocks as snippet_blocks
from wagtail.snippets.models import register_snippet

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

    color1 = models.CharField(max_length=7, default='#d9b058')
    color2 = models.CharField(max_length=7, default='#a37146')

    motto_de = RichTextField(blank=True)
    motto_en = RichTextField(blank=True)

    area_de = models.CharField(max_length=256)
    area_en = models.CharField(max_length=256)

    image = models.ForeignKey(
        'images.CustomImage',
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
        FieldPanel('color1'),
        FieldPanel('color2')
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
    personlist = core_blocks.ListBlock(PersonDisplayBlock)

    class Meta:
        template = 'persons/person_list.html'
        icon = 'snippet'
        label = 'Person Import'


class AllPersonsBlock(core_blocks.StructBlock):
    headline = core_blocks.CharBlock(required=False)

    class Meta:
        template = 'persons/all_persons_list.html'
