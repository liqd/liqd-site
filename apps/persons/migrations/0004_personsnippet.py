# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('persons', '0003_auto_20160407_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonSnippet',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('motto_de', wagtail.core.fields.RichTextField(blank=True)),
                ('motto_en', wagtail.core.fields.RichTextField(blank=True)),
                ('area_de', models.CharField(max_length=256)),
                ('area_en', models.CharField(max_length=256)),
                ('image', models.ForeignKey(related_name='+', to='wagtailimages.Image', null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL)),
            ],
        ),
    ]
