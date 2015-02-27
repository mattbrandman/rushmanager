from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^rushtracker/', include('rushtracker.urls', namespace="rushtracker")),
    url(r'^events/', include('events.urls', namespace="events")),
    url(r'^comments/', include('comments.urls', namespace="comments")),
	url(r'^authentication/', include('authentication.urls', namespace="authentication")),
    url(r'^admin/', include(admin.site.urls)),
)