from django.conf.urls import patterns, url
from organization import views

urlpatterns = patterns('', 
	#the carrot and dollar sign are there to ensure what is 
	#searched is exactly what is found in regex
	url(r'^overview/$|^$', views.OrganizationOverview.as_view(), name='createOrganization'),
	url(r'^update/$', views.SetActiveRushPeriod.as_view(), name='setActiveRushPeriod'),
	)