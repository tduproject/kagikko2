# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 23:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('grade', models.CharField(max_length=5)),
                ('major', models.CharField(max_length=5)),
                ('text', models.TextField()),
            ],
        ),
    ]
