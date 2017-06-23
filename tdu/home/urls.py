from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.show, name='show'),
    url(r'^contact/$', views.contact, name='contact'),
]
