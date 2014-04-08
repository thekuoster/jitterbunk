from django.conf.urls import patterns, url

from bunks import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<user_id>\d+)/bunk/$', views.bunk, name='bunk'),
)