from django.conf.urls import patterns, include, url
from chaptermanagement.views import IndexView

urlpatterns = patterns('',
	url(r'^$', IndexView.as_view()),
)