# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-19 12:13
from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.db import migrations


def update_tags(apps, schema_editor):
    TaggedItem = apps.get_model("taggit", "TaggedItem")
    WagtailImage = apps.get_model("wagtailimages", "Image")
    CustomImage = apps.get_model("images", "CustomImage")

    wagtail_image_ct = ContentType.objects.get_for_model(WagtailImage)
    custom_image_ct = ContentType.objects.get_for_model(CustomImage)

    for tag in TaggedItem.objects.all():
        if tag.content_type_id == wagtail_image_ct.pk:
            tag.content_type_id = custom_image_ct.pk
            tag.save()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_addresssettings_custom_image"),
    ]

    operations = [migrations.RunPython(update_tags)]
