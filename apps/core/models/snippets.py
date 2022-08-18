from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import (FieldPanel, InlinePanel,
                                         PageChooserPanel)
from wagtail.models import Orderable
from wagtail.snippets.models import register_snippet

from contrib.translations.translations import TranslatedField


class LinkFields(models.Model):
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='+',
        on_delete=models.CASCADE
    )

    @property
    def link(self):
        return self.link_page.url

    panels = [
        PageChooserPanel('link_page')
    ]

    class Meta:
        abstract = True


class MenuItem(LinkFields):
    menu_title_de = models.CharField(
        max_length=255, verbose_name="Menu Title de")
    menu_title_en = models.CharField(
        max_length=255, blank=True, verbose_name="Menu Title en")

    translated_menu_title = TranslatedField(
        'menu_title_de',
        'menu_title_en',
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
