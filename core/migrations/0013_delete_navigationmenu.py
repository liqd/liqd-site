# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20160229_1000'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NavigationMenu',
        ),
    ]
