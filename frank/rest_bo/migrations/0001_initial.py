# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.DateTimeField(max_length=50)),
                ('description', models.CharField(max_length=255, null=True)),
                ('level', models.PositiveSmallIntegerField(null=True)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
    ]
