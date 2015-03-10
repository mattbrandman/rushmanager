from django.conf.urls import patterns, include, url
from rushperiod.views import IndexView, CreateRushPeriodView

urlpatterns = patterns('',
	url(r'^$', IndexView.as_view(), name='index'),
	url(r'^create$', CreateRushPeriodView.as_view(), name='create'),
)