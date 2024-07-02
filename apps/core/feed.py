from django.contrib.syndication.views import Feed

from apps.blog.models import BlogPage


class LatestEntriesFeed(Feed):
    title = "Liquid Democracy Blogposts"
    link = "/"

    def items(self):
        return BlogPage.objects.all().live().order_by("-date")[:5]

    def item_title(self, item):
        return item.translated_title

    def item_description(self, item):
        return item.translated_intro

    def item_link(self, item):
        return item.url
