#profilesの全てのviewをインポートするよ
from django.conf.urls import include, url
from . import views

urlpatterns = [
               url(r'^detail/(?P<pk>[0-9]+)/$', views.profile_detail, name = 'profile_detail'),
               url(r'^edit/$', views.profile_edit, name='profile_edit'),
               url(r'^mydetail/$', views.profile_mydetail, name = 'profile_mydetail'),
               ]
