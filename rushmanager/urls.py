from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^rushtracker/', include('rushtracker.urls', namespace="rushtracker")),
    url(r'^admin/', include(admin.site.urls)),
)