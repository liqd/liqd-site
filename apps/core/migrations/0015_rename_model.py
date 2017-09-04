# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-06 09:13
from __future__ import unicode_literals

import apps.core.blocks
import apps.persons.models
from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0039_collectionviewrestriction'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('core', '0014_auto_20170628_1747'),
    ]

    operations = [
        migrations.RenameModel("JoinUsPage", "TextPageWithBlocks")
    ]