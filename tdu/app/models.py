from datetime import datetime
from django.db import models



class Post(models.Model):
    title = models.CharField('曜日', max_length=255)
    text = models.CharField('時間', max_length=255)
    sub = models.CharField('科目名', max_length=255)
    category = models.CharField('カテゴリ名', max_length=255 ,default='SOME STRING')
    when = models.CharField('時期', max_length=255 ,default='SOME STRING')

    def __str__(self):
        return self.sub
