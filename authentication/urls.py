from django.conf.urls import patterns, url
from authentication import views
from authentication.forms import AuthenticationFormAny

urlpatterns = patterns('', 
	#the carrot and dollar sign are there to ensure what is 
	#searched is exactly what is found in regex
	url(r'^sign_up$', views.SignUpFormView.as_view(), name='sign_up'),
	url(r'^sign_in$', 'django.contrib.auth.views.login', {'template_name' : 'authentication/sign_in.html', 
		'authentication_form' : AuthenticationFormAny}, name='sign_in'),
	url(r'^sign_out$', 'django.contrib.auth.views.logout_then_login', name='sign_out')
	
)