# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-03 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20170703_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
    ]
