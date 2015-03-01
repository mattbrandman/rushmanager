from django.conf.urls import patterns, url
from organization import views

urlpatterns = patterns('', 
	#the carrot and dollar sign are there to ensure what is 
	#searched is exactly what is found in regex
	url(r'^new/$', views.OrganizationCreateView.as_view(), name='createOrganization'),
	url(r'^organization_home/$', views.OrganizationHome.as_view(), name='organization_home'),
	)