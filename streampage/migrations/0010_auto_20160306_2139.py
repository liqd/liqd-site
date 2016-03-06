# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('streampage', '0009_auto_20160306_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joinuspage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='JoinUsPage',
        ),
    ]
