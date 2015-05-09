from django.conf.urls import patterns, url
from ranking.views import createRank

urlpatterns = patterns('', 
	#the carrot and dollar sign are there to ensure what is 
	#searched is exactly what is found in regex
	url(r'^$', createRank.as_view()),
)