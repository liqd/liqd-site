# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0001_initial'),
        ('wagtailforms', '0001_initial'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('wagtailsearch', '0001_initial'),
        ('core', '0003_auto_20150529_0824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogindexpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='blogindexpagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='blogindexpagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='blogindexpagerelatedlink',
            name='page',
        ),
        migrations.DeleteModel(
            name='BlogIndexPage',
        ),
        migrations.DeleteModel(
            name='BlogIndexPageRelatedLink',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='author',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='blogpagecarouselitem',
            name='image',
        ),
        migrations.RemoveField(
            model_name='blogpagecarouselitem',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='blogpagecarouselitem',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='blogpagecarouselitem',
            name='page',
        ),
        migrations.DeleteModel(
            name='BlogPageCarouselItem',
        ),
        migrations.RemoveField(
            model_name='blogpagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='blogpagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='blogpagerelatedlink',
            name='page',
        ),
        migrations.DeleteModel(
            name='BlogPageRelatedLink',
        ),
        migrations.RemoveField(
            model_name='blogpagetag',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='blogpagetag',
            name='tag',
        ),
        migrations.DeleteModel(
            name='BlogPageTag',
        ),
        migrations.RemoveField(
            model_name='blogparagraph',
            name='page',
        ),
        migrations.DeleteModel(
            name='BlogPage',
        ),
        migrations.DeleteModel(
            name='BlogParagraph',
        ),
        migrations.RemoveField(
            model_name='personindexpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='PersonIndexPage',
        ),
        migrations.RemoveField(
            model_name='personpage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='personpage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='personpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='personpagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='personpagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='personpagerelatedlink',
            name='page',
        ),
        migrations.DeleteModel(
            name='PersonPage',
        ),
        migrations.DeleteModel(
            name='PersonPageRelatedLink',
        ),
    ]
