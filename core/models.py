from wagtail.wagtailcore.models import Page, Orderable
from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailadmin.edit_handlers import InlinePanel
from wagtail.wagtailadmin.edit_handlers import PageChooserPanel

from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailsnippets.models import register_snippet

from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailadmin.edit_handlers import TabbedInterface, ObjectList, MultiFieldPanel

from wagtail.contrib.settings.models import BaseSetting, register_setting

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

from core import blocks

from contrib.translations.translations import TranslatedField


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
        help_text='Responsive image slider (swipe on mobile). Please choose 4 images.')),
    ('columns', blocks.ColumnBlock()),
    ('linkbox', blocks.LinkboxBlock()),
    ('project_teaser', blocks.ProjectTeaserBlock()),
]

class TranslatedStreamFieldPage(Page):

    title_en = models.CharField(max_length=255, blank=True, verbose_name="Header Title")
    title_de = models.CharField(max_length=255, blank=True, verbose_name="Header Title")

    intro_en = RichTextField(blank=True)
    intro_de = RichTextField(blank=True)

    body_en = StreamField(STREAMFIELD_DEFAULT_BLOCKS, null=True)
    body_de = StreamField(STREAMFIELD_DEFAULT_BLOCKS, null=True, blank=True)


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

    class Meta:
        verbose_name = 'Extended Page'
        managed = True
        abstract = True


class JoinUsPage(TranslatedStreamFieldPage):

    class Meta:
        verbose_name = 'default header and streamfield'

    subpage_types = ['JoinUsPage', 'TextPage']



class HomePage(TranslatedStreamFieldPage):

    heading1_en = models.CharField(max_length=255, default="")
    heading1_de = models.CharField(max_length=255, default="")
    
    heading2_en = models.CharField(max_length=255, default="")
    heading2_de = models.CharField(max_length=255, default="")

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
        heading = "Slug and CMS Page Name"),
        MultiFieldPanel([
            FieldPanel('seo_title'),
            FieldPanel('search_description'),
        ],
        heading = "SEO settings de",
        classname="collapsible")
    ]

    edit_handler = TabbedInterface([
        ObjectList(de_content_panels, heading='Content de'),
        ObjectList(en_content_panels, heading='Content en'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    ])

    subpage_types = ['JoinUsPage', 'TextPage']


class TextPage(Page):
    
    title_en = models.CharField(max_length=255, blank=True, verbose_name="Header Title")
    title_de = models.CharField(max_length=255, blank=True, verbose_name="Header Title")

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

    subpage_types = ['TextPage']


class PressPage(Page):
    intro = RichTextField(blank=True)

    #subpage_types = []

PressPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full")
]



@register_snippet
class PressLink(models.Model):
    url = models.URLField(null=True)
    source = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date = models.DateField("Post date")

    panels = [
        FieldPanel('url'),
        FieldPanel('source'),
        FieldPanel('title'),
        FieldPanel('date')
    ]

    def __unicode__(self):
        return self.source + ', ' + self.title


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
    menu_title = models.CharField(max_length=255, verbose_name="Menu Title en")
    menu_title_de = models.CharField(max_length=255, blank=True, verbose_name="Menu Title de")

    translated_menu_title = TranslatedField(
        'menu_title_de',
        'menu_title',
    )

    @property
    def url(self):
        return self.link

    def __str__(self):
        return self.title

    panels = [
        FieldPanel('menu_title_de'),
        FieldPanel('menu_title'),
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



@register_setting
class LiqdSettings(BaseSetting):
    liqd_preliminary_site = models.BooleanField(
        default=False,
        help_text="Phase One of the new site, this setting can be deleted when the full site is ready to go live",
    )
