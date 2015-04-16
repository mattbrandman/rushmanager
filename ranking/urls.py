from django.conf.urls import patterns, url
from ranking.views import createRank, submitRank

urlpatterns = patterns('', 
	#the carrot and dollar sign are there to ensure what is 
	#searched is exactly what is found in regex
	url(r'^create/$', createRank.as_view()),
	url(r'^submit/$', submitRank.as_view()),
)