# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('taggit', '0001_initial'),
        ('blog', '0001_initial'),
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='author',
            field=models.ForeignKey(related_name='blogpages', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='persons.PersonPage', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpage',
            name='feed_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(to='taggit.Tag', through='blog.BlogPageTag', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
