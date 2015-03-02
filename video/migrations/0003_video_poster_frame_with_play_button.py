# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20150301_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='poster_frame_with_play_button',
            field=models.ImageField(help_text=b'Poster frame for the video with a play button superimposed on it.', null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
