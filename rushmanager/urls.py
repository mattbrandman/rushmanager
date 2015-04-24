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
# Serializers define the API representation.


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'is_staff', 'is_rush_committee', 'id', 'password',)
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = self.context['user']
        request = self.context['request']
        print validated_data
        if validated_data['password'] != request.data['confirm']:
            raise serializers.ValidationError("Passwords Do Not Match")
        new_user = get_user_model().objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            organization=user.organization
            )
        user_profile = UserProfile(user=new_user)
        user_profile.save()
        return new_user

# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = get_user_model()
    def get_queryset(self):
        return get_user_model().tenant_objects.all().order_by('-is_rush_committee', 'email')

    def create(self, request):
        serializer = UserSerializer(data=request.data, context={'user':request.user, 'request':request})
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
    rush  = RushSerializer(read_only=True)
    class Meta:
        model = Ranking
        read_only_fields=('rush',)

class RankedViewSet(viewsets.ModelViewSet):
    model = Ranking
    serializer_class = RankingSerializer
    permission_classes = [permissions.IsAuthenticated, SameOrganizationPermission]
    def get_queryset(self): 
        return self.request.user.profile.ranking.all()

    @detail_route(methods=['post'], permission_classes=[], url_path='delete-rank')
    def delete_rank(self, request,  pk=None):
        rank = self.get_object()
        print rank
        if rank.userprofile_set.all()[:1].get().user.id == self.request.user.id:
            rank.delete()
            return Response({
                'message': 'successful deletion'
                })
        return Response ({
            'message': 'failed to delete'
            })
    

class RankListViewSet(viewsets.ViewSet):
    """
    Returns the rankings of the kids 

    """
    permission_classes=[permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        correct_org = Q(rush__organization = request.user.organization)
        is_rush_comm = Q(userprofile__user__is_rush_committee = True)
        print Ranking.objects.filter(is_rush_comm)
        all_rankings = Ranking.objects.filter(correct_org & is_rush_comm)
        all_rushes = Rush.tenant_objects.all()
        rankList = []
        rank = {}
        for rush in all_rushes:
            specific_rank_value = all_rankings.filter(rush__id=rush.id).aggregate(Sum('rank'))
            specific_rank_value = specific_rank_value['rank__sum']
            if specific_rank_value != None:
                number_of_rankings = all_rankings.filter(rush__id=rush.id).count()
                average_rank = specific_rank_value/number_of_rankings

                rankList.append({
                    'rush': RushSerializer(rush).data,
                    'rank': average_rank
                    })

        return Response(rankList)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    model = Comment
    def get_queryset(self):
        return Comment.objects.filter(user__id = self.request.user.id)


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, 'Users')
router.register(r'rush', RushViewSet, 'Rush')
router.register(r'rushRanking', RushViewSetRanked, 'unranked')
router.register(r'ranked', RankedViewSet, 'RushRanked')
router.register(r'generate-rank-list', RankListViewSet, 'RankingGeneration')
router.register(r'comments', CommentViewSet, 'comment')


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

