from django import template
from django.core.urlresolvers import resolve
from django.http import Http404

from core.models import NavigationMenu

register = template.Library()


# include menu tag
@register.assignment_tag(takes_context=False)
def load_site_menu(menu_name):
    menu = NavigationMenu.objects.filter(menu_name=menu_name)

    if menu:
        return menu[0].menu_items.all()
    else:
        return None


@register.simple_tag(takes_context=True, name='translate_url')
def do_translate_url(context, language):
    try:
        view = resolve(context['request'].path)
        if view.args:
            url = '/' + language + '/' + view.args[0]
        else:
            url = '/' + language + '/'
    except Http404:
        url = '/' + language + '/'
    return url
