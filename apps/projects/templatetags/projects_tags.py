from django import template

register = template.Library()


@register.inclusion_tag('projects/project_teaser.html')
def project_teaser(teaser, request):
    return {
        'teaser': teaser,
        'request': request
    }
