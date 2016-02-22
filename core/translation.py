from .models import HomePage
from .models import TextPage
from wagtail_modeltranslation.translation import TranslationOptions
from wagtail_modeltranslation.decorators import register

@register(HomePage)
class HomePageTR(TranslationOptions):
    fields = (
    	'heading',
    	'intro',
        'body',
    )

@register(TextPage)
class TextPageTR(TranslationOptions):
    fields = (
    	'title',
        'body',
    )
