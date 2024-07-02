from .abstract_page_model import TranslatedStreamFieldPage


class TextPageWithBlocks(TranslatedStreamFieldPage):

    class Meta:
        verbose_name = "Default Page with several Blocks"

    subpage_types = ["TextPageWithBlocks", "TextPage"]
