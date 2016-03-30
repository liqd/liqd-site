from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from blog.models import BlogPage

class LatestEntriesFeed(Feed):
    title = "Liquid Democracy site news"
    link = "/blog/"

    def items(self):
        return BlogPage.objects.all().live().order_by('-date')[:5]

    def item_title(self, item):
        return item.translated_title

    def item_description(self, item):
        return item.translated_intro

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return item.url