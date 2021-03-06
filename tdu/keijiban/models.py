from django.db import models


class Posting(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='名前',
        help_text='あなたの名前を入力してください',
     )
    message = models.TextField(
         verbose_name='メッセージ',
         help_text='メッセージを入力してください',
         null=True,
     )
    subject = models.CharField(
        max_length=64,
        verbose_name='科目名',
        null=True,
     )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='登録日時',
    )
    pk_label = models.IntegerField(
        null=True,
    )

class PostingSubject(models.Model):
    subject = models.CharField(
        max_length=64,
        verbose_name='科目名',
        null=True,
     )
