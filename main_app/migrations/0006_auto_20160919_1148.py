# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20160916_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treasure',
            name='image',
            field=models.ImageField(default='media/treasure_images/default.png', upload_to='treasure_images'),
        ),
    ]
