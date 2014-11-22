# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rest_bo', '0008_auto_20141122_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='path',
            field=models.CharField(default=datetime.datetime(2014, 11, 22, 7, 53, 21, 747562, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
