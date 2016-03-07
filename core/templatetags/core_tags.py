from django import template
from core.models import PressLink
from core.models import NavigationMenu
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


# include menu tag
@register.assignment_tag(takes_context=False)
def load_site_menu(menu_name):
    menu = NavigationMenu.objects.filter(menu_name=menu_name)

    if menu:
        return menu[0].menu_items.all()
    else:
        return None