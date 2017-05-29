# coding: UTF-8
from django.conf.urls import  url

from polls import views

urlpatterns = [
 url(r'^$', views.poll_list),

 url(r'^poll/(?P<pk>[0-9]+)/$', views.poll_detail, name = 'poll_detail'),
  # ex: /polls/5/
  # ex: /polls/5/results/
  url(r'^vote/$', views.vote, name='vote'),
  # ex: /polls/5/vote/
  #url(r'^result/$',views.result,name='result'),
]
