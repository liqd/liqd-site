from django import template
from core.models import PressLink
from django.db import connections
from django.db.models import Count

register = template.Library()


# press snippets tags
@register.inclusion_tag('core/tags/press_snippets.html', takes_context=True)
def press_snippets(context):
    return {
        'press_snippets': PressLink.objects.all().order_by('-date'),
        'request': context['request']
    }
