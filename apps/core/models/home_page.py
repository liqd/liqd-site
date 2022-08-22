from wagtail.admin.panels import (FieldPanel, MultiFieldPanel, ObjectList,
                                  TabbedInterface)
from wagtail.models import Page

from .abstract_page_model import TranslatedStreamFieldPage


class HomePage(TranslatedStreamFieldPage):
    en_content_panels = [
        FieldPanel('intro_en'),
        FieldPanel('body_en'),
    ]

    de_content_panels = [
        FieldPanel('intro_de'),
        FieldPanel('body_de'),
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

    subpage_types = ['TextPageWithBlocks', 'TextPage',
                     'projects.ProjectIndexPage', 'blog.BlogIndexPage',
                     'academy.AcademyIndexPage',
                     'academy.AcademyChallengePage',
                     'academy.AcademyLandingPage']
