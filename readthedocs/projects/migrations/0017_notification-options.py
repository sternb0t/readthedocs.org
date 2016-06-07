# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_build-queue-name'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailhook',
            name='send_on_failure',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='emailhook',
            name='send_on_success',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='webhook',
            name='send_on_failure',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='webhook',
            name='send_on_success',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='has_valid_webhook',
            field=models.BooleanField(default=False, help_text='This project has been built with a webhook'),
        ),
    ]
