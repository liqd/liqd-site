from django import template

from apps.persons.models import PersonSnippet

register = template.Library()


@register.simple_tag(takes_context=False)
def get_all_persons():
    return PersonSnippet.objects.all().order_by('last_name')
