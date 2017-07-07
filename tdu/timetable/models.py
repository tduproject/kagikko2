from datetime import datetime
from django.db import models

class Timetable1(models.Model):
    username = models.CharField('名前', max_length=255)
    day = models.CharField('曜日', max_length=255)
    time = models.CharField('時間', max_length=255)
    sub = models.CharField('科目名', max_length=255)
    when = models.CharField('時期', max_length=255)

    def __str__(self):
        return self.username

class Timetable2(models.Model):
    username = models.CharField('名前', max_length=255)
    day = models.CharField('曜日', max_length=255)
    time = models.CharField('時間', max_length=255)
    sub = models.CharField('科目名', max_length=255)
    when = models.CharField('時期', max_length=255)

    def __str__(self):
        return self.username
