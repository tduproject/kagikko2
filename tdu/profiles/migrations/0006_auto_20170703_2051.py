# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-03 20:51
from __future__ import unicode_literals

from django.db import migrations
import encrypted_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20170703_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='grade',
            field=encrypted_fields.fields.EncryptedIntegerField(),
        ),
    ]