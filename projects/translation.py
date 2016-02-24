from .models import ProjectIndexPage
from wagtail_modeltranslation.translation import TranslationOptions
from wagtail_modeltranslation.decorators import register


@register(ProjectIndexPage)
class ProjectIndexPageTR(TranslationOptions):
    fields = (
    	'title',
        'intro',
    )
