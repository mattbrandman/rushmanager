from django.conf.urls import patterns, include, url
from django.contrib import admin
from rushtracker.views import IndexView
from django.contrib.auth.views import get_user_model
from rest_framework import routers, serializers, viewsets, permissions
from django.conf import settings
from rushtracker.models import Rush
from ranking.models import Ranking
from rest_framework.response import Response

# Serializers define the API representation.


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('email', 'is_staff', 'is_rush_committee', 'id', 'password')
        write_only_fields = ('password',)
    def create(self, validated_data):
        user = self.context['user']
        print validated_data
        new_user = get_user_model().objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            organization=user.organization
            )
        return new_user

# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = get_user_model()
    def get_queryset(self):
        return get_user_model().tenant_objects.all()
    def create(self, request):
        serializer = UserSerializer(data=request.data, context={'user':request.user,})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    # cache is causing the old list to be returned.  override
    # get query set to fix


class RushSerializer(serializers.ModelSerializer):

	class Meta:
		model = Rush
		fields = ('first_name', 'last_name', 'id')


class RushViewSet(viewsets.ModelViewSet):
    serializer_class = RushSerializer
    model = Rush
    def get_queryset(self):
        return Rush.tenant_objects.all()

class RushViewSetRanked(viewsets.ModelViewSet):
    model = Rush
    serializer_class = RushSerializer

    def get_queryset(self):
        already_ranked = self.request.user.profile.ranking.values('rush')
        not_ranked = Rush.tenant_objects.exclude(pk__in=already_ranked)
        return not_ranked


class RankingSerializer(serializers.ModelSerializer):
    rush  = RushSerializer()
    class Meta:
        model = Ranking

class RankedViewSet(viewsets.ModelViewSet):
    model = Ranking
    serializer_class = RankingSerializer
    def get_queryset(self):
        return self.request.user.profile.ranking.all()

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, 'Users')
router.register(r'rush', RushViewSet, 'Rush')
router.register(r'rushRanking', RushViewSetRanked, 'RushUnranked')
router.register(r'ranked', RankedViewSet, 'RushRanked')


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

