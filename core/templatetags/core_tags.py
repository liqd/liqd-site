from django import template

register = template.Library()


# persons tags
@register.inclusion_tag('core/includes/person_list.html', takes_context=True)
def persons(context):
  return {
    'adverts': Advert.objects.all(),
    'request': context['request'],
  }