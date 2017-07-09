from django.conf.urls import  url

from .import views

urlpatterns = [
 url(r'^$', views.time_table, name = 'table'), #追加 7/9 山田
 url(r'^timeedit/$', views.time_table2, name='edit'),
 url(r'^result/$', views.show, name='result'),
]
