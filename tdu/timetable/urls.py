from django.conf.urls import  url

from .import views

urlpatterns = [
 url(r'^$', views.time_table),
 url(r'^timeedit/$', views.time_table2, name='edit'),
 url(r'^result/$', views.show, name='result'),
]
