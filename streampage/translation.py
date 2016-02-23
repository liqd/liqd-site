from .models import StreamPage
from .models import JoinUsPage
from wagtail_modeltranslation.translation import TranslationOptions
from wagtail_modeltranslation.decorators import register


# @register(StreamPage)
# class StreamPageTR(TranslationOptions):
#     fields = (
#         'title',
#         'intro',
#         'body',
#     )


@register(JoinUsPage)
class JoinUsPageTR(TranslationOptions):
    fields = (
        'title',
        'intro',
        'body',
    )