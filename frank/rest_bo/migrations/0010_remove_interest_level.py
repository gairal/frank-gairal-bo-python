# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_bo', '0009_auto_20141122_0753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interest',
            name='level',
        ),
    ]
