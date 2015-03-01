# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text=b'The full name of the video.', max_length=100)),
                ('slug', models.SlugField(help_text=b'A short identifier for the video, used in URLs and such. Only letters, numbers, underscores, and hyphens are allowed.', unique=True)),
                ('description', models.TextField(help_text=b'Description of the video. Can contain HTML.')),
                ('source', models.FileField(help_text=b'Source file for the video. Must be video/mp4.', upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
