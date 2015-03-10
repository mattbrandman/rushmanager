from django.conf.urls import patterns, include, url
from django.contrib import admin
from rushtracker.views import IndexView

urlpatterns = patterns('',
	url(r'^$', IndexView.as_view()),
	url(r'^rushtracker/', include('rushtracker.urls', namespace="rushtracker")),
    url(r'^events/', include('events.urls', namespace="events")),
    url(r'^comments/', include('comments.urls', namespace="comments")),
	url(r'^authentication/', include('authentication.urls', namespace="authentication")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^organization/', include('organization.urls', namespace="organization")),
    url(r'^chaptermanagement/', include('chaptermanagement.urls', namespace="chaptermanagement")),
    url(r'^rushperiod/', include('rushperiod.urls', namespace="rushperiod")),
)