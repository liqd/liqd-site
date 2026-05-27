from wagtail.fields import StreamField

from .abstract_page_model import STREAMFIELD_SIMPLE_PAGE_BLOCKS
from .abstract_page_model import TranslatedStreamFieldPage


class TextPageWithBlocks(TranslatedStreamFieldPage):
    body_en = StreamField(
        STREAMFIELD_SIMPLE_PAGE_BLOCKS,
        null=True,
        blank=True,
        verbose_name="Body",
        use_json_field=True,
    )
    body_de = StreamField(
        STREAMFIELD_SIMPLE_PAGE_BLOCKS,
        null=True,
        blank=True,
        verbose_name="Body",
        use_json_field=True,
    )

    class Meta:
        verbose_name = "Default Page with several Blocks"

    subpage_types = ["TextPageWithBlocks", "TextPage"]
