from django import template
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.http import Http404
from django.urls import resolve

from apps.core.models import NavigationMenu

register = template.Library()


# include menu tag
@register.simple_tag(takes_context=False)
def load_site_menu(menu_name):
    menu = NavigationMenu.objects.filter(menu_name=menu_name)

    if menu:
        return menu[0].menu_items.all()
    else:
        return None


@register.simple_tag(takes_context=True, name="translate_url")
def do_translate_url(context, language):
    try:
        view = resolve(context["request"].path)
        if view.args:
            url = "/" + language + "/" + view.args[0]
        else:
            url = "/" + language + "/"
        if context["request"].GET:
            url += "?" + context["request"].GET.urlencode()
    except Http404:
        url = "/" + language + "/"
    return url


@register.simple_tag
def combined_url_parameter(request_query_dict, **kwargs):
    combined_query_dict = request_query_dict.copy()
    for key in kwargs:
        combined_query_dict.setlist(key, [kwargs[key]])
    encoded_parameter = "?" + combined_query_dict.urlencode()
    return encoded_parameter


@register.simple_tag
def file_type(media_file):
    if media_file.endswith(".mp4"):
        return "video/mp4"
    elif media_file.endswith(".webm"):
        return "video/webm"
    elif media_file.endswith(".mp3"):
        return "audio/mp3"
    elif media_file.endswith(".wav"):
        return "audio/wav"
    else:
        return "type invalid"


@register.simple_tag()
def matomo_enabled():
    if hasattr(settings, "MATOMO_ENABLED"):
        return settings.MATOMO_ENABLED
    return False


@register.inclusion_tag("matomo/tracking_code.html")
def matomo_tracking_code():
    if not hasattr(settings, "MATOMO_SITE_ID"):
        raise ImproperlyConfigured("MATOMO_SITE_ID does not exist.")

    if not hasattr(settings, "MATOMO_URL"):
        raise ImproperlyConfigured("MATOMO_URL does not exist.")

    cookie_disabled = True
    if hasattr(settings, "MATOMO_COOKIE_DISABLED"):
        cookie_disabled = settings.MATOMO_COOKIE_DISABLED

    return {
        "id": settings.MATOMO_SITE_ID,
        "url": settings.MATOMO_URL,
        "cookie_disabled": cookie_disabled,
    }
