from django.conf.urls import patterns, include, url
from chaptermanagement.views import IndexView, BrotherModal

urlpatterns = patterns('',
	url(r'^$', IndexView.as_view()),
	url(r'^add_brother_modal$', BrotherModal.as_view(), name='brother_modal'),
)