from django import template

from blog.models import BlogPage

register = template.Library()


@register.inclusion_tag('blog/tags/blogentries.html', takes_context=True)
def blog_entries(context):
    return {
        'blog_entries': BlogPage.objects.all().live().order_by('-date')[:2],
        'request': context['request']
    }
