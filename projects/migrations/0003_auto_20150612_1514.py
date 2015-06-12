# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
        ('projects', '0002_auto_20150612_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectpersons',
            name='body',
        ),
        migrations.RemoveField(
            model_name='projectpersons',
            name='image',
        ),
        migrations.RemoveField(
            model_name='projectpersons',
            name='title',
        ),
        migrations.RemoveField(
            model_name='projectpersons',
            name='visible',
        ),
        migrations.AddField(
            model_name='projectpersons',
            name='person',
            field=models.ForeignKey(default=1, to='persons.PersonPage'),
            preserve_default=False,
        ),
    ]
