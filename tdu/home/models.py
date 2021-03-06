from django.db import models

# Create your models here.

class Contact(models.Model):
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
    title = models.CharField(
        max_length=64,
        verbose_name='ご用件',
        null=True,
     )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='登録日時',
    )
