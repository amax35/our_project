# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_remove_photo_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='url',
            field=models.Field(),
        ),
    ]
