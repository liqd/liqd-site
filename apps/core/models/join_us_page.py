from .abstract_page_model import TranslatedStreamFieldPage


class JoinUsPage(TranslatedStreamFieldPage):

    class Meta:
        verbose_name = 'Default Page with several Blocks'

    subpage_types = ['JoinUsPage', 'TextPage']
