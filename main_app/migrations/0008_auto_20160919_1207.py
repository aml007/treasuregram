# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20160919_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treasure',
            name='image',
            field=models.FileField(default='treasure_images/default.png', upload_to='treasure_images'),
        ),
    ]
