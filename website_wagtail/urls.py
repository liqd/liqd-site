import os

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from wagtail.contrib.sitemaps.views import sitemap as wagtail_sitemap

from apps.core.feed import LatestEntriesFeed

urlpatterns = [
    url(r'^django-admin/', admin.site.urls),
    url(r'^admin/', include('wagtail.admin.urls')),
    url(r'^documents/', include('wagtail.documents.urls')),
    url(r'^robots\.txt$', TemplateView.as_view(
        template_name='robots.txt',
        content_type="text/plain"), name="robots_file"),
              ]

urlpatterns += i18n_patterns(
    # url(r'^search/', include('wagtail.search.urls')),
    url(r'^latest/feed/$', LatestEntriesFeed()),
    url(r'^sitemap\.xml$', wagtail_sitemap),

    url(r'', include('wagtail.core.urls')),
)


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL + 'images/',
                          document_root=os.path.join(
                              settings.MEDIA_ROOT, 'images'))
