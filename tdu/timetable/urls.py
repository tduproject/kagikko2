from django.conf.urls import  url

from timetable import views

urlpatterns = [
 url(r'^$', views.time_table),
 url(r'^timeedit/$', views.time_table2, name='edit'),
]
