# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20160916_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treasure',
            name='image',
            field=models.ImageField(default='default.png', upload_to='treasure_images/'),
        ),
    ]