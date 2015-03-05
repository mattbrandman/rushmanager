from django.conf.urls import patterns, url
from rushtracker import views

urlpatterns = patterns('', 
	#the carrot and dollar sign are there to ensure what is 
	#searched is exactly what is found in regex
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^update/(?P<pk>\d+)/$', views.UpdateView.as_view(), name='update'),
	url(r'^create_rush$', views.RushCreateView.as_view(), name='create_rush'),	
    url(r'^rush/detail/(?P<pk>\d+)/$', views.RushDetailView.as_view(), name='rush_detail'),
)