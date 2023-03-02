from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin import edit_handlers
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.core.blocks import CharBlock, PageChooserBlock, StructBlock
from wagtail.core.fields import StreamField
from wagtail.models import Orderable
from wagtail.snippets.models import register_snippet

from contrib.translations.translations import (TranslatedField,
                                               TranslatedStructValue)


class TranslatedLinkBlock(StructBlock):
    link = PageChooserBlock()
    link_text_de = CharBlock(max_length=255)
    link_text_en = CharBlock(max_length=255)

    class Meta:
        value_class = TranslatedStructValue


class LinkFields(models.Model):
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='+',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        return None

    panels = [
        FieldPanel('link_page')
    ]

    class Meta:
        abstract = True


class MenuItem(LinkFields):
    menu_title_de = models.CharField(
        max_length=255, verbose_name="Menu Title de")
    menu_title_en = models.CharField(
        max_length=255, verbose_name="Menu Title en")

    translated_menu_title = TranslatedField(
        'menu_title_de',
        'menu_title_en',
    )

    subpages = StreamField(
        [
            ('submenuitem', TranslatedLinkBlock())
        ],
        use_json_field=True,
        blank=True,
        null=True,
        help_text=(
            'These links will be displayed in a second level navigation.'
        ),
        verbose_name='Submenu',
        max_num=5
    )

    @property
    def url(self):
        return self.link

    def __str__(self):
        return self.title

    panels = [
        FieldPanel('menu_title_de'),
        FieldPanel('menu_title_en'),
    ] + LinkFields.panels
    panels.append(edit_handlers.FieldPanel('subpages'))


@register_snippet
class NavigationMenu(ClusterableModel):

    menu_name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.menu_name

    panels = [
        FieldPanel('menu_name', classname='full title'),
        InlinePanel('menu_items', label="Menu Items")
    ]


class NavigationMenuItem(Orderable, MenuItem):
    parent = ParentalKey('core.NavigationMenu', related_name='menu_items')


@register_snippet
class BlogCategory(models.Model):
    name_en = models.CharField(max_length=255)
    name_de = models.CharField(max_length=255, blank=True, null=True)
    translated_name = TranslatedField('name_de', 'name_en')

    panels = [
        FieldPanel('name_en'),
        FieldPanel('name_de'),
    ]

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name_plural = 'blog categories'


@register_snippet
class ProjectCategory(models.Model):
    name_en = models.CharField(max_length=255)
    name_de = models.CharField(max_length=255, blank=True, null=True)
    translated_name = TranslatedField('name_de', 'name_en')

    panels = [
        FieldPanel('name_en'),
        FieldPanel('name_de')
    ]

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name_plural = 'project categories'
