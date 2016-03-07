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
        FieldPanel('slug'),
        MultiFieldPanel([
            FieldPanel('seo_title'),
            FieldPanel('search_description'),
        ],
        heading = "SEO settings de",
        classname="collapsible"),
        # MultiFieldPanel([
        #     FieldPanel('seo_title'),
        #     FieldPanel('search_description'),
        # ],
        # heading = "SEO settings en",
        # classname="collapsible")
    ]

    edit_handler = TabbedInterface([
        # ObjectList(content_panels, heading='Content'),
        ObjectList(en_content_panels, heading='Content en'),
        ObjectList(de_content_panels, heading='Content de'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    ])

    class Meta:
        verbose_name = 'Extended Page'
        managed = True
        abstract = True


class JoinUsPage(TranslatedStreamFieldPage):

    class Meta:
        verbose_name = 'JoinUs Page'



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
    
    # intro_en = RichTextField(blank=True)
    # intro_de = RichTextField(blank=True)

    # body_en = StreamField(
    #     STREAMFIELD_DEFAULT_BLOCKS
    #     [
    #     # ('heading', blocks.CharBlock(classname="full title", icon="title")),
    #     ('standard_paragraph', blocks.StructBlock(
    #         [
    #             ('headline', blocks.CharBlock(required=False, length=256)),
    #             ('text', blocks.RichTextBlock(required=True)),
    #         ],
    #         template="blocks/block_standard_paragraph.html",
    #         icon="pilcrow",
    #         help_text="Standard paragraph"
    #         )
    #     ),
    #     # ('image', ImageChooserBlock(icon="image")),
    #     ('highlight_paragraph', blocks.StructBlock(
    #         [
    #             ('headline', blocks.CharBlock(required=False, length=256)),
    #             ('text', blocks.RichTextBlock(required=True)),
    #             ('link', blocks.PageChooserBlock(required=False)),
    #         ],
    #         template="blocks/block_highlight_paragraph.html",
    #         icon="pilcrow",
    #         help_text="Paragraph with grey background. Use this as linkbox also (e.g. job offers)."
    #         )
    #     ),
    #     ('quote_paragraph', blocks.StructBlock(
    #         [
    #             ('text', blocks.RichTextBlock(required=True)),
    #             ('color',blocks.ChoiceBlock(
    #                 choices=[('green','Gruen'),('orange','Orange'),('red','Rot')],
    #                 required=True,
    #                 help_text="Select a color from the listself."
    #             ))
    #         ], 
    #         template="blocks/block_quote_paragraph_image.html",
    #         icon="pilcrow",
    #         help_text="Textquote with background color."
    #         )
    #     ),
    #     ('quote_paragraph_image', blocks.StructBlock(
    #         [
    #             ('text', blocks.RichTextBlock(required=True)),
    #             ('image', ImageChooserBlock(
    #                 icon="image",
    #                 required=True,
    #                 help_text="Please use an image with at least 813x400px and a similar aspect ratio."
    #                 )),
    #         ],
    #         template="blocks/block_quote_paragraph_image.html",
    #         icon="pilcrow",
    #         help_text="Textquote with background image."
    #         )
    #     ),
    #     ('project_teaser', blocks.StructBlock(
    #         [
    #             ('title', blocks.CharBlock(required=False, length=256)),
    #             ('shorttext', blocks.RichTextBlock(required=True)),
    #             ('image', ImageChooserBlock(icon="image")),
    #             ('slug', blocks.PageChooserBlock(
    #                 help_text="Please choose an internal page from the list."
    #                 )
    #             ),
    #             ('external_url', blocks.CharBlock(required=False, length=256)),
    #         ],
    #         template="blocks/block_project_teaser.html",
    #         icon="pilcrow",
    #         help_text="Generic teaser / Project teaser with manual content"
    #         )
    #     ),

    # ]
    # , null=True)
    # body_en = StreamField(STREAMFIELD_DEFAULT_BLOCKS, null=True, blank=True)

    # content_panels = Page.content_panels + [
    #     FieldPanel('heading1_de'),
    #     FieldPanel('heading2'),
    #     FieldPanel('intro'),
    #     StreamFieldPanel('body'),
    # ]

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
        FieldPanel('slug'),
        MultiFieldPanel([
            FieldPanel('seo_title'),
            FieldPanel('search_description'),
        ],
        heading = "SEO settings de",
        classname="collapsible")
    ]
    # promote_panels = [
    #     FieldPanel('slug'),
    #     MultiFieldPanel([
    #         FieldPanel('seo_title_de'),
    #         FieldPanel('search_description_de'),
    #     ],
    #     heading = "SEO settings de",
    #     classname="collapsible"),
        # MultiFieldPanel([
        #     FieldPanel('seo_title_en'),
        #     FieldPanel('search_description_en'),
        # ],
        # heading = "SEO settings en",
        # classname="collapsible")
    # ]

    edit_handler = TabbedInterface([
        ObjectList(en_content_panels, heading='Content en'),
        ObjectList(de_content_panels, heading='Content de'),
        ObjectList(promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    ])


class TextPage(Page):
    
    title_en = models.CharField(max_length=255, blank=True, verbose_name="Header Title")
    title_de = models.CharField(max_length=255, blank=True, verbose_name="Header Title")

    body_en = RichTextField(blank=True)
    body_de = RichTextField(blank=True)

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
        FieldPanel('slug'),
        MultiFieldPanel([
            FieldPanel('seo_title'),
            FieldPanel('search_description'),
        ],
        heading = "SEO settings",
        classname="collapsible"),
        # MultiFieldPanel([
        #     FieldPanel('seo_title'),
        #     FieldPanel('search_description'),
        # ],
        # heading = "SEO settings en",
        # classname="collapsible")
    ]

    edit_handler = TabbedInterface([
        ObjectList(en_content_panels, heading='Content en'),
        ObjectList(de_content_panels, heading='Content de'),
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
