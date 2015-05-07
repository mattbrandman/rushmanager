from django.conf.urls import patterns, include, url
from django.contrib import admin
from rushtracker.views import IndexView
from django.contrib.auth.views import get_user_model
from rest_framework import routers, serializers, viewsets, permissions, views, generics
from django.conf import settings
from rushtracker.models import Rush
from ranking.models import Ranking
from authentication.models import UserProfile
from django.db.models import Sum
from rest_framework.response import Response
from django.db.models import Q
from comments.models import Comment
from rest_framework import serializers, permissions
from rest_framework.decorators import detail_route
from authentication.permissions import SameOrganizationPermission
from api import serializers
# Serializers define the API representation.

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', serializers.UserViewSet, 'Users')
router.register(r'rush', serializers.RushViewSet, 'rush')
router.register(r'rushRanking', serializers.RushViewSetRanked, 'unranked')
router.register(r'ranked', serializers.RankViewSet, 'RushRanked')
router.register(r'generate-rank-list', serializers.RankListViewSet, 'RankingGeneration')
router.register(r'comments', serializers.CommentViewSet, 'comment')
router.register(r'events', serializers.EventViewSet, 'event')
router.register(r'organization', serializers.OrganizationViews, 'organization')
router.register(r'rushperiod', serializers.RushPeriodViews, 'rushperiod')

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
	url(r'^api/', include(router.urls)),
	url(r'^rushtracker/', include('rushtracker.urls', namespace="rushtracker")),
    url(r'^events/', include('events.urls', namespace="events")),
    url(r'^comments/', include('comments.urls', namespace="comments")),
	url(r'^authentication/', include('authentication.urls', namespace="authentication")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^organization/', include('organization.urls', namespace="organization")),
    url(r'^chaptermanagement/', include('chaptermanagement.urls', namespace="chaptermanagement")),
    url(r'^rushperiod/', include('rushperiod.urls', namespace="rushperiod")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^ranking/', include('ranking.urls', namespace="ranking")),
)

