from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(
        help_text='Your Facebook page URL', blank=True)
    twitter = models.CharField(
        max_length=255, help_text='Your twitter username,'
        ' without the @', blank=True)
    github = models.URLField(
        help_text='Your Github organisation page URL', blank=True)
    vimeo = models.URLField(
        help_text='Link to your vimeo account', blank=True)


@register_setting
class AddressSettings(BaseSetting):
    organisation_name = models.CharField(
        max_length=255, help_text='The name of your organisation')
    organisation_street = models.CharField(
        max_length=255, help_text='Streetname and housenumber '
        'of your organisations office ')
    postalcode = models.CharField(
        max_length=255, help_text='postalcode and city')
    telephone_number = models.CharField(max_length=255, blank=True)
    email_address = models.EmailField(max_length=70, blank=True)

    image = models.ForeignKey(
        'images.CustomImage',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='+'
    )

    panels = [
        FieldPanel('organisation_name'),
        FieldPanel('organisation_street'),
        FieldPanel('postalcode'),
        FieldPanel('telephone_number'),
        FieldPanel('email_address'),
        ImageChooserPanel('image')
    ]
