# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_bo', '0005_skill_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('short_description', models.CharField(max_length=255, null=True)),
                ('year_in', models.DateField()),
                ('year_out', models.DateField(null=True)),
                ('place', models.CharField(max_length=50)),
                ('diploma', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('extra_info', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
            ],
            options={
                'ordering': ('year_in',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('description', models.TextField()),
                ('date_in', models.DateField()),
                ('date_out', models.DateField(null=True)),
                ('place', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=100)),
                ('accomplishments', models.TextField()),
                ('display_order', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ('date_in',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('description', models.CharField(max_length=50, null=True)),
                ('level', models.PositiveSmallIntegerField(null=True)),
                ('display_order', models.PositiveSmallIntegerField()),
                ('category', models.ForeignKey(related_name='interests', to='rest_bo.Category')),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place', models.CharField(unique=True, max_length=50)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('display_order', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ('place',),
            },
            bases=(models.Model,),
        ),
    ]
