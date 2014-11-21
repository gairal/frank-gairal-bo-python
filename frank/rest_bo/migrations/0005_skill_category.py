# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_bo', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(related_name='skills', default=1, to='rest_bo.Category'),
            preserve_default=False,
        ),
    ]
