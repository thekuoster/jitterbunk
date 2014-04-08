from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^bunks/', include('bunks.urls', namespace="bunks")),
    url(r'^admin/', include(admin.site.urls)),
)
