# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_bo', '0010_remove_interest_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='name',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
