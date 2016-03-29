from django import template
from django.http import Http404
from django.core.urlresolvers import reverse
from django.core.urlresolvers import resolve
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


@register.inclusion_tag('projects/project_teaser.html')
def project_teaser(teaser, request):
    return {
        'teaser': teaser,
        'request': request
    }


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
