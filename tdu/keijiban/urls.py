from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='list'),
    url(r'^create/$', views.create_thread, name='create'),
    url(r'^index/(?P<pk>[0-9]+)/$', views.index, name='index'),
]
