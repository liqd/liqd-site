# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('core', '0009_auto_20160222_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiqdSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('liqd_preliminary_site', models.BooleanField(default=False, help_text=b'Phase One of the new site, this setting can be deleted when the full site is ready to go live')),
                ('site', models.OneToOneField(editable=False, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
