# coding: UTF-8
from django.db import models

#
# アンケート質問モデル
#

class Poll(models.Model):
  subname = models.CharField(max_length=200)
  question1 = models.CharField(max_length=200)
  question2 = models.CharField(max_length=200)
  question3 = models.CharField(max_length=200)

def __str__(self):
    return self.subname


#
# アンケート選択モデル
#
class Choice(models.Model):
  subname = models.CharField(max_length=200, default='SOME STRING')
  value = models.CharField(max_length=200 , default='SOME STRING')
  easy = models.IntegerField(default=0)
  normal = models.IntegerField(default=0)
  hard = models.IntegerField(default=0)

  def __str__(self):
    return self.subname
