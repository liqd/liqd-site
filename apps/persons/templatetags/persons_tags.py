from apps.persons.models import PersonSnippet
from django import template

register = template.Library()

@register.assignment_tag(takes_context=False)
def get_all_persons():
    return PersonSnippet.objects.all().order_by('last_name')
