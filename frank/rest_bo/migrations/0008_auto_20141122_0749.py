# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_bo', '0007_auto_20141121_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('path', models.CharField(max_length=255, null=True)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='education',
            name='image',
            field=models.ForeignKey(related_name='educations', to='rest_bo.Image', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experience',
            name='image',
            field=models.ForeignKey(related_name='experiences', to='rest_bo.Image', null=True),
            preserve_default=True,
        ),
    ]
