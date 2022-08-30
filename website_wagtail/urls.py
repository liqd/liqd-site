import os

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from wagtail.contrib.sitemaps.views import sitemap as wagtail_sitemap

from apps.core.feed import LatestEntriesFeed

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('admin/', include('wagtail.admin.urls')),
    path('documents/', include('wagtail.documents.urls')),
    re_path(r'^robots\.txt$',
            TemplateView.as_view(template_name='robots.txt',
                                 content_type="text/plain"),
            name="robots_file"),
]

urlpatterns += i18n_patterns(
    # url(r'^search/', include('wagtail.search.urls')),
    path('latest/feed/', LatestEntriesFeed()),
    re_path(r'^sitemap\.xml$', wagtail_sitemap),
    path('', include('wagtail.urls')),
)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL + 'images/',
                          document_root=os.path.join(settings.MEDIA_ROOT,
                                                     'images'))
