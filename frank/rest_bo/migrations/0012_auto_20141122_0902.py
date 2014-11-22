# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_bo', '0011_auto_20141122_0831'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('display_order',)},
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ('-year_in',)},
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ('-date_in',)},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={},
        ),
        migrations.AlterModelOptions(
            name='interest',
            options={'ordering': ('display_order',)},
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={},
        ),
        migrations.AlterModelOptions(
            name='travel',
            options={'ordering': ('display_order',)},
        ),
    ]
