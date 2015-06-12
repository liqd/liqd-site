# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtaildocs', '0002_initial_data'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('taggit', '0001_initial'),
        ('core', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True,
                                                  primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.wagtailcore.fields.RichTextField(
                    blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogIndexPageRelatedLink',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(
                    null=True, editable=False, blank=True)),
                ('link_external', models.URLField(
                    verbose_name=b'External link', blank=True)),
                ('title', models.CharField(
                    help_text=b'Link title', max_length=255)),
                ('link_document', models.ForeignKey(
                    related_name='+', blank=True, to='wagtaildocs.Document', null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True,
                                                  primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.RichTextField()),
                ('subtitle', models.CharField(
                    max_length=255, null=True, blank=True)),
                ('author_string', models.CharField(
                    max_length=255, null=True, blank=True)),
                ('date', models.DateField(verbose_name=b'Post date')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogPageCarouselItem',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(
                    null=True, editable=False, blank=True)),
                ('link_external', models.URLField(
                    verbose_name=b'External link', blank=True)),
                ('embed_url', models.URLField(
                    verbose_name=b'Embed URL', blank=True)),
                ('caption', models.CharField(max_length=255, blank=True)),
                ('image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL,
                                            blank=True, to='wagtailimages.Image', null=True)),
                ('link_document', models.ForeignKey(
                    related_name='+', blank=True, to='wagtaildocs.Document', null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogPageRelatedLink',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(
                    null=True, editable=False, blank=True)),
                ('link_external', models.URLField(
                    verbose_name=b'External link', blank=True)),
                ('title', models.CharField(
                    help_text=b'Link title', max_length=255)),
                ('link_document', models.ForeignKey(
                    related_name='+', blank=True, to='wagtaildocs.Document', null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogPageTag',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_object', modelcluster.fields.ParentalKey(
                    related_name='tagged_items', to='core.BlogPage')),
                ('tag', models.ForeignKey(
                    related_name='core_blogpagetag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogParagraph',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(
                    null=True, editable=False, blank=True)),
                ('title', models.CharField(
                    help_text=b'Title', max_length=255)),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('page', modelcluster.fields.ParentalKey(
                    related_name='paragraphs', to='core.BlogPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True,
                                                  primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.wagtailcore.fields.RichTextField(
                    blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PersonPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True,
                                                  primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('telephone', models.CharField(max_length=20, blank=True)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('biography', wagtail.wagtailcore.fields.RichTextField(
                    blank=True)),
                ('area', models.CharField(max_length=256, choices=[(b'Vorstand', b'Vorstand'), (
                    b'Projektmanagement', b'Projektmanagement'), (b'Entwicklung', b'Entwicklung'), (b'Design', b'Design')])),
                ('feed_image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL,
                                                 blank=True, to='wagtailimages.Image', null=True)),
                ('image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL,
                                            blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='PersonPageRelatedLink',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(
                    null=True, editable=False, blank=True)),
                ('link_external', models.URLField(
                    verbose_name=b'External link', blank=True)),
                ('title', models.CharField(
                    help_text=b'Link title', max_length=255)),
                ('link_document', models.ForeignKey(
                    related_name='+', blank=True, to='wagtaildocs.Document', null=True)),
                ('link_page', models.ForeignKey(
                    related_name='+', blank=True, to='wagtailcore.Page', null=True)),
                ('page', modelcluster.fields.ParentalKey(
                    related_name='related_links', to='core.PersonPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blogpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(
                related_name='+', blank=True, to='wagtailcore.Page', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(
                related_name='related_links', to='core.BlogPage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpagecarouselitem',
            name='link_page',
            field=models.ForeignKey(
                related_name='+', blank=True, to='wagtailcore.Page', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpagecarouselitem',
            name='page',
            field=modelcluster.fields.ParentalKey(
                related_name='carousel_items', to='core.BlogPage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpage',
            name='author',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.SET_NULL, blank=True, to='core.PersonPage', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpage',
            name='feed_image',
            field=models.ForeignKey(
                related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(
                to='taggit.Tag', through='core.BlogPageTag', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogindexpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(
                related_name='+', blank=True, to='wagtailcore.Page', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogindexpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(
                related_name='related_links', to='core.BlogIndexPage'),
            preserve_default=True,
        ),
    ]
