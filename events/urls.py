from django.conf.urls import patterns, url
from events import views

urlpatterns = patterns('', 
    url(r'^new$', views.EventCreateView.as_view(), name='create_event'),  
)