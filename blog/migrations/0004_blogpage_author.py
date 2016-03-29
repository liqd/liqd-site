# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0004_auto_20160318_1748'),
        ('blog', '0003_remove_blogpage_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='author',
            field=models.ForeignKey(related_name='blogpages', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='persons.PersonPage', null=True),
        ),
    ]
