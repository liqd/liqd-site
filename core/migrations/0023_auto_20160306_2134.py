# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('core', '0022_joinpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joinpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='JoinPage',
        ),
    ]
