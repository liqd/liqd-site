# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-12 13:39
from __future__ import unicode_literals

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_blogcategory_projectcategory"),
        ("projects", "0006_remove-heading"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="projectindexpage",
            options={"verbose_name": "Project List"},
        ),
        migrations.AddField(
            model_name="projectpage",
            name="categories",
            field=modelcluster.fields.ParentalManyToManyField(
                blank=True, to="core.ProjectCategory"
            ),
        ),
    ]
