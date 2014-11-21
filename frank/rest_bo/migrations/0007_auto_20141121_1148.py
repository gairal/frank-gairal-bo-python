# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_bo', '0006_education_experience_interest_travel'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='skills',
            field=models.ManyToManyField(to='rest_bo.Skill'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experience',
            name='skills',
            field=models.ManyToManyField(to='rest_bo.Skill'),
            preserve_default=True,
        ),
    ]
