from wagtail.wagtailcore.models import Page, Orderable
from django.db import models
from streampage.models import StreamPage


from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailadmin.edit_handlers import InlinePanel
from wagtail.wagtailadmin.edit_handlers import PageChooserPanel

from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailsnippets.models import register_snippet

from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock

from wagtail_modeltranslation.models import TranslationMixin
from wagtail.wagtailadmin.edit_handlers import TabbedInterface, ObjectList, MultiFieldPanel

from wagtail.contrib.settings.models import BaseSetting, register_setting

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

# from contrib.translations.translations import TranslatedField


class HomePage(Page):
    heading1 = models.CharField(max_length=255, default="")
    heading2 = models.CharField(max_length=255, default="")
    intro = RichTextField(blank=True)
    body = StreamField([
        # ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('standard_paragraph', blocks.StructBlock(
            [
                ('headline', blocks.CharBlock(required=False, length=256)),
                ('text', blocks.RichTextBlock(required=True)),
            ],
            template="blocks/block_standard_paragraph.html",
            icon="pilcrow",
            help_text="Standard paragraph"
            )
        ),
        # ('image', ImageChooserBlock(icon="image")),
        ('highlight_paragraph', blocks.StructBlock(
            [
                ('headline', blocks.CharBlock(required=False, length=256)),
                ('text', blocks.RichTextBlock(required=True)),
                ('link', blocks.PageChooserBlock(required=False)),
            ],
            template="blocks/block_highlight_paragraph.html",
            icon="pilcrow",
            help_text="Paragraph with grey background. Use this as linkbox also (e.g. job offers)."
            )
        ),
        ('quote_paragraph', blocks.StructBlock(
            [
                ('text', blocks.RichTextBlock(required=True)),
                ('color',blocks.ChoiceBlock(
                    choices=[('green','Gruen'),('orange','Orange'),('red','Rot')],
                    required=True,
                    help_text="Select a color from the listself."
                ))
            ], 
            template="blocks/block_quote_paragraph_image.html",
            icon="pilcrow",
            help_text="Textquote with background color."
            )
        ),
        ('quote_paragraph_image', blocks.StructBlock(
            [
                ('text', blocks.RichTextBlock(required=True)),
                ('image', ImageChooserBlock(
                    icon="image",
                    required=True,
                    help_text="Please use an image with at least 813x400px and a similar aspect ratio."
                    )),
            ],
            template="blocks/block_quote_paragraph_image.html",
            icon="pilcrow",
            help_text="Textquote with background image."
            )
        ),
        ('project_teaser', blocks.StructBlock(
            [
                ('title', blocks.CharBlock(required=False, length=256)),
                ('shorttext', blocks.RichTextBlock(required=True)),
                ('image', ImageChooserBlock(icon="image")),
                ('slug', blocks.PageChooserBlock(
                    help_text="Please choose an internal page from the list."
                    )
                ),
                ('external_url', blocks.CharBlock(required=False, length=256)),
            ],
            template="blocks/block_project_teaser.html",
            icon="pilcrow",
            help_text="Generic teaser / Project teaser with manual content"
            )
        ),

    ], null=True)

    content_panels = Page.content_panels + [
        FieldPanel('heading1'),
        FieldPanel('heading2'),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
    ]
    # de_content_panels = [
    #     FieldPanel('heading_de'),
    #     FieldPanel('intro_de'),
    #     StreamFieldPanel('body_de'),
    # ]

    # en_content_panels = [
    #     FieldPanel('heading_en'),
    #     FieldPanel('intro_en'),
    #     StreamFieldPanel('body_en'),
    # ]

    # promote_panels = [
    #     FieldPanel('slug'),
    #     MultiFieldPanel([
    #         FieldPanel('seo_title_de'),
    #         FieldPanel('search_description_de'),
    #     ],
    #     heading = "SEO settings de",
    #     classname="collapsible"),
    #     MultiFieldPanel([
    #         FieldPanel('seo_title_en'),
    #         FieldPanel('search_description_en'),
    #     ],
    #     heading = "SEO settings en",
    #     classname="collapsible")
    # ]

    # edit_handler = TabbedInterface([
    #     # ObjectList(content_panels, heading='Content'),
    #     ObjectList(de_content_panels, heading='Content de'),
    #     ObjectList(en_content_panels, heading='Content en'),
    #     ObjectList(promote_panels, heading='Promote'),
    #     ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    # ])


class TextPage(TranslationMixin, Page):
    
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('title_de'),
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
        FieldPanel('slug'),
        MultiFieldPanel([
            FieldPanel('seo_title_de'),
            FieldPanel('search_description_de'),
        ],
        heading = "SEO settings de",
        classname="collapsible"),
        MultiFieldPanel([
            FieldPanel('seo_title_en'),
            FieldPanel('search_description_en'),
        ],
        heading = "SEO settings en",
        classname="collapsible")
    ]

    edit_handler = TabbedInterface([
        # ObjectList(content_panels, heading='Content'),
        ObjectList(de_content_panels, heading='Content de'),
        ObjectList(en_content_panels, heading='Content en'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    ])


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
    menu_title = models.CharField(max_length=255)
#     menu_title_de = models.CharField(max_length=255, blank=True)
#     menu_title_it = models.CharField(max_length=255, blank=True)
#     menu_title_fr = models.CharField(max_length=255, blank=True)
#     menu_title_sv = models.CharField(max_length=255, blank=True)
#     menu_title_sl = models.CharField(max_length=255, blank=True)
#     menu_title_da = models.CharField(max_length=255, blank=True)

    # translated_menu_title = TranslatedField(
    #     'menu_title_de',
    #     'menu_title_it',
    #     'menu_title',
    #     'menu_title_fr',
    #     'menu_title_sv',
    #     'menu_title_sl',
    #     'menu_title_da',
    # )

    @property
    def url(self):
        return self.link

    def __str__(self):
        return self.title

    panels = [
        FieldPanel('menu_title'),
        # MultiFieldPanel(
        #     [
    #             FieldPanel('menu_title_de'),
    #             FieldPanel('menu_title_it'),
    #             FieldPanel('menu_title_fr'),
    #             FieldPanel('menu_title_sv'),
    #             FieldPanel('menu_title_sl'),
    #             FieldPanel('menu_title_da'),
    #         ],
    #         heading="Translations",
    #         classname="collapsible collapsed"
    #     )
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
