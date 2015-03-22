from django.conf.urls import patterns, url
from events import views

urlpatterns = patterns('', 
    url(r'^new$', views.EventCreateView.as_view(), name='create_event'),  
    url(r'^all_events$', views.EventIndexView.as_view(), name='all_events'),
    url(r'^take_attendance$', views.EventAttendanceView.as_view(), name='take_attendance'),  
)