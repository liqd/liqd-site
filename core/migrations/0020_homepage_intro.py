# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20160306_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='intro',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
