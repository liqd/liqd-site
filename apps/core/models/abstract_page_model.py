from django.db import models
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, MultiFieldPanel,
                                                ObjectList, StreamFieldPanel,
                                                TabbedInterface)
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.blocks import ImageChooserBlock

from apps.core import blocks
from apps.persons import models as persons_models
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
                                      help_text='Responsive image slider'
                                      ' (swipe on mobile). Please choose'
                                      ' 4 images.')),
    ('aligned_image', blocks.AlignedImageBlock()),
    ('columns', blocks.ColumnBlock()),
    ('linkbox', blocks.LinkboxBlock()),
    ('projects', blocks.TeaseredProjectsBlock()),
    ('ThreeImageLinks', blocks.ThreeImageWithLinkBlock()),
    ('Raw_HTML', blocks.HTMLBlock()),
    ('Person', persons_models.PersonListBlock()),
    ('all_persons_list', persons_models.AllPersonsBlock()),
    ('teaser_list', blocks.TeaserBlockList())

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
