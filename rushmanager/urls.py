from django.conf.urls import patterns, include, url
from django.contrib import admin
from rushtracker.views import IndexView
from django.contrib.auth.views import get_user_model
from rest_framework import routers, serializers, viewsets, permissions
from django.conf import settings
from rushtracker.models import Rush

# Serializers define the API representation.


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('email', 'is_staff')

# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class RushSerializer(serializers.ModelSerializer):

	class Meta:
		model = Rush
		fields = ('first_name', 'last_name', 'id')


class RushViewSet(viewsets.ModelViewSet):
	queryset = Rush.tenant_objects.all()
	serializer_class = RushSerializer

class RushViewSetForRankings(viewsets.ModelViewSet):
    model = Rush
    serializer_class = RushSerializer
    def get_queryset(self):
        not_ranked = self.request.user.profile.ranking.values('rush')
        already_ranked = Rush.tenant_objects.exclude(pk__in=not_ranked)
        return already_ranked
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'rush', RushViewSet)
router.register(r'rushRanking', RushViewSetForRankings, 'RushRanking')

urlpatterns = patterns('',
	url(r'^api/', include(router.urls)),
	url(r'^$', IndexView.as_view()),
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

