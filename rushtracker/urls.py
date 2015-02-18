from django.conf.urls import patterns, url
from rushtracker import views
from rushtracker.forms import AuthenticationFormAny
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('', 
	#the carrot and dollar sign are there to ensure what is 
	#searched is exactly what is found in regex
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.UpdateView.as_view(), name='update'),
	url(r'^sign_up$', views.SignUpFormView.as_view(), name='sign_up'),
	url(r'^create_rush$', views.RushCreateView.as_view(), name='create_rush'),
	url(r'^sign_in$', 'django.contrib.auth.views.login', {'template_name' : 'rushtracker/sign_in.html', 
		'authentication_form' : AuthenticationFormAny}, name='sign_in'),
	url(r'^sign_out$', 'django.contrib.auth.views.logout_then_login', name='sign_out')

)