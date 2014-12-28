from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'uSystem.views.index', name='Home'),
    url(r'^admin/', include(admin.site.urls)),
)
