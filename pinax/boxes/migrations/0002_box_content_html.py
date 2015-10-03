# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boxes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='content_html',
            field=models.TextField(blank=True),
        ),
    ]
