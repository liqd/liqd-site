# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20160307_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='menu_title_de',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
