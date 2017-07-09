from django.conf.urls import url
from . import views


urlpatterns = [
    #会員登録
    url(r'^create/$', views.CreateUserView.as_view(), name='create'),
    url(r'^create_done/$', views.CreateDoneView.as_view(), name='create_done'),
    url(r'^create_complete/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.CreateCompleteView.as_view(), name='create_complete'),

    #ログイン ログアウト
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),

    #パスワードリセット
    url(r'^password_reset/$', views.password_reset, name='password_reset'),
    url(r'^password_reset_done/$', views.password_reset_done,name='password_reset_done'),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password_reset_complete/$', views.password_reset_complete, name='password_reset_complete'),

]
