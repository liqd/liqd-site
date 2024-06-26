# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-15 14:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def set_custom_image_id(apps, schema_editor):
    CustomImage = apps.get_model("images", "CustomImage")
    AddressSettings = apps.get_model("core", "AddressSettings")

    for address_setting in AddressSettings.objects.all():
        if address_setting.image:
            image = address_setting.image
            address_setting.custom_image_id = CustomImage.objects.get(
                id=image.id
            )
            address_setting.save()


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0002_copy_images"),
        ("core", "0010_remove-icon"),
    ]

    operations = [
        migrations.AddField(
            model_name="addresssettings",
            name="custom_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.CustomImage",
            ),
        ),
        migrations.RunPython(set_custom_image_id),
        migrations.RemoveField(
            model_name="addresssettings",
            name="image",
        ),
        migrations.RenameField(
            model_name="addresssettings",
            old_name="custom_image",
            new_name="image",
        ),
    ]
