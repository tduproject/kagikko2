# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-03 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='あなたの名前を入力してください', max_length=64, verbose_name='名前')),
                ('message', models.TextField(help_text='メッセージを入力してください', null=True, verbose_name='メッセージ')),
                ('subject', models.CharField(max_length=64, null=True, verbose_name='科目名')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
            ],
        ),
        migrations.CreateModel(
            name='PostingSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=64, null=True, verbose_name='科目名')),
            ],
        ),
    ]
