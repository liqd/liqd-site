from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, InlinePanel,
                                                MultiFieldPanel, ObjectList,
                                                PageChooserPanel,
                                                StreamFieldPanel,
                                                TabbedInterface)
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsnippets.models import register_snippet

from contrib.translations.translations import TranslatedField
from core import blocks
from persons import models as persons_models

STREAMFIELD_DEFAULT_BLOCKS = [
    ('standard_paragraph', blocks.StandardParagraphBlock()),
    ('highlight_paragraph', blocks.HighlightParagraphBlock()),
    ('quote_paragraph', blocks.QuoteParagraph()),
    ('single_image', ImageChooserBlock(
        template='blocks/block_image.html',
        label='Single image',
        icon='image')),
    ('image_slider', blocks.ListBlock(ImageChooserBlock(),
                                      template='blocks/block_carousel.html',
                                      label='Image Slider',
                                      icon='image',
                                      help_text='Responsive image slider'
                                      ' (swipe on mobile). Please choose'
                                      ' 4 images.')),
    ('columns', blocks.ColumnBlock()),
    ('linkbox', blocks.LinkboxBlock()),
    ('project_teaser', blocks.ProjectTeaserBlock()),
    ('ThreeImageLinks', blocks.ThreeImageWithLinkBlock()),
    ('Raw_HTML', blocks.HTMLBlock()),
    ('Person', persons_models.PersonListBlock())
]


class TranslatedStreamFieldPage(Page):

    title_en = models.CharField(max_length=255, verbose_name="Title")
    title_de = models.CharField(
        max_length=255, blank=True, verbose_name="Title")

    intro_en = RichTextField(blank=True, verbose_name="Teasertext")
    intro_de = RichTextField(blank=True, verbose_name="Teasertext")

    body_en = StreamField(STREAMFIELD_DEFAULT_BLOCKS,
                          null=True, verbose_name="Body")
    body_de = StreamField(STREAMFIELD_DEFAULT_BLOCKS,
                          null=True, blank=True, verbose_name="Body")

    body = TranslatedField(
        'body_de',
        'body_en'
    )

    translated_title = TranslatedField(
        'title_de',
        'title_en',
    )

    translated_intro = TranslatedField(
        'intro_de',
        'intro_en',
    )

    de_content_panels = [
        FieldPanel('title_de'),
        FieldPanel('intro_de'),
        StreamFieldPanel('body_de'),
    ]

    en_content_panels = [
        FieldPanel('title_en'),
        FieldPanel('intro_en'),
        StreamFieldPanel('body_en'),
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
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings',
                   classname="settings"),
    ])

    class Meta:
        verbose_name = 'Extended Page'
        managed = True
        abstract = True


class JoinUsPage(TranslatedStreamFieldPage):

    class Meta:
        verbose_name = 'Default header and streamfield Page'

    subpage_types = ['JoinUsPage', 'TextPage']


class HomePage(TranslatedStreamFieldPage):

    heading1_en = models.CharField(
        max_length=255, default="", verbose_name="Title top")
    heading1_de = models.CharField(
        max_length=255, default="", blank=True, verbose_name="Title top")

    heading2_en = models.CharField(
        max_length=255, default="", verbose_name="Title bottom")
    heading2_de = models.CharField(
        max_length=255, default="", blank=True, verbose_name="Title bottom")

    translated_heading1 = TranslatedField(
        'heading1_de',
        'heading1_en',
    )

    translated_heading2 = TranslatedField(
        'heading2_de',
        'heading2_en',
    )

    en_content_panels = [
        FieldPanel('heading1_en'),
        FieldPanel('heading2_en'),
        FieldPanel('intro_en'),
        StreamFieldPanel('body_en'),
    ]

    de_content_panels = [
        FieldPanel('heading1_de'),
        FieldPanel('heading2_de'),
        FieldPanel('intro_de'),
        StreamFieldPanel('body_de'),
    ]

    promote_panels = [
        MultiFieldPanel([
            FieldPanel('slug'),
            FieldPanel('title'),
        ],
            heading="Slug and CMS Page Name"),
        MultiFieldPanel([
            FieldPanel('seo_title'),
            FieldPanel('search_description'),
        ],
            heading="SEO settings de",
            classname="collapsible")
    ]

    edit_handler = TabbedInterface([
        ObjectList(en_content_panels, heading='English'),
        ObjectList(de_content_panels, heading='German'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings',
                   classname="settings"),
    ])

    subpage_types = ['JoinUsPage', 'TextPage',
                     'projects.ProjectIndexPage', 'blog.BlogIndexPage']


class TextPage(Page):

    title_en = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title")
    title_de = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title")

    body_en = RichTextField(blank=True)
    body_de = RichTextField(blank=True)

    body = TranslatedField(
        'body_de',
        'body_en'
    )

    translated_title = TranslatedField(
        'title_de',
        'title_en',
    )

    content_panels = Page.content_panels + [
        FieldPanel('title'),
    ]

    de_content_panels = [
        FieldPanel('title_de'),
        FieldPanel('body_de'),
    ]

    en_content_panels = [
        FieldPanel('title_en'),
        FieldPanel('body_en'),
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
        ObjectList(en_content_panels, heading='Content en'),
        ObjectList(de_content_panels, heading='Content de'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings',
                   classname="settings"),
    ])

    subpage_types = ['TextPage']


class LinkFields(models.Model):
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='+'
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
