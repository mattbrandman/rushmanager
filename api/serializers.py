from rest_framework import serializers, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from django.contrib.auth import get_user_model
from rushtracker.models import Rush
from comments.models import Comment
from ranking.models import Ranking
from organization.models import Organization
from rushperiod.models import RushPeriod
from authentication.permissions import SameOrganizationPermission
from django.contrib.auth.models import Permission
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from authentication.models import UserProfile



class UserSerializer(serializers.ModelSerializer):
    confirm = serializers.CharField(max_length=50, write_only=True)
    class Meta:
        model = get_user_model()
        fields =  ('email', 'is_staff', 'is_rush_committee', 'id', 'password', 'confirm',)
        extra_kwargs = {
            'password': {'write_only': True},
        }
    def create(self, validated_data):
        user = self.context['user']
        request = self.context['request']
        if validated_data['password']  == validated_data['confirm']:
            new_user = get_user_model().objects.create_user(
                email=validated_data['email'],
                password=validated_data['password'],
                organization=user.organization
            )
            user_profile = UserProfile(user=new_user)
            user_profile.save()
            print new_user
            return new_user


# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = get_user_model()

    def get_queryset(self):
        return get_user_model().tenant_objects.all().order_by('-is_rush_committee', 'email')

    def create(self, request):
        if not isinstance(request.data, list):
            is_many = False
        else:
            is_many = True
        serializer = UserSerializer(
            data=request.data, context={'user': request.user, 'request': request}, many=is_many)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @detail_route(methods=['patch'], url_path='change-rush-comm-status')
    def change_rush_comm(self, request, pk=None):
        user = self.get_object()
        user.is_rush_committee = not user.is_rush_committee
        perm_add = Permission.objects.get(codename='add_ranking')
        perm_delete = Permission.objects.get(codename='delete_ranking')
        if not user.is_rush_committee:
            user.user_permissions.remove(perm_add)
            user.user_permissions.remove(perm_delete)
        else:
            user.user_permissions.add(perm_add)
            user.user_permissions.add(perm_delete)
        user.save()
        return Response(UserSerializer(user).data)
    def list(self, request):
        return  super(UserViewSet,self).list(request)
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
    #returns unranked kids
    model = Rush
    serializer_class = RushSerializer

    def get_queryset(self):
        already_ranked = self.request.user.profile.ranking.values('rush')
        not_ranked = Rush.tenant_objects.exclude(pk__in=already_ranked)
        return not_ranked


class RankSerializer(serializers.ModelSerializer):
    rush = RushSerializer()
    class Meta:
        model = Ranking
        depth = 1
        fields = ('rush', 'rank', 'id')
    def create(self, validated_data):
        user = self.context['user']
        request = self.context['request']
        print request.data
        rush = get_object_or_404(Rush, pk=request.data['rush']['id'])
        if rush.organization == user.organization:
            rank = Ranking(user=user, rush=rush, rank=validated_data['rank'], organization = user.organization)
            rank.save()
            return rank
        raise serializers.ValidationError("you are not in the same organization")

class RankViewSet(viewsets.ModelViewSet):
    #returns ranked kids
    model = Ranking
    serializer_class = RankSerializer
    permission_classes = [
        permissions.IsAuthenticated, SameOrganizationPermission]

    def get_queryset(self):
        return Ranking.tenant_objects.filter(user__id=self.request.user.id)
   

    def create(self, request):
        serializer = RankSerializer(
            data=request.data, context={'user': request.user, 'request': request})
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
    @list_route(methods=['get'], url_path="get-unranked")
    def get_unranked(self, request):
        already_ranked = Ranking.tenant_objects.filter(user__id=request.user.id).values('rush')
        unranked = Rush.tenant_objects.exclude(pk__in=already_ranked)
        data = RushSerializer(unranked, many=True).data
        return Response(data)

class RankListViewSet(viewsets.ViewSet):
    model = Ranking

    """
    Returns the rankings of the kids 

    """
    def list(self, request, *args, **kwargs):
        all_rankings = Ranking.tenant_objects.filter(user__is_rush_committee=True)
        all_rushes = Rush.tenant_objects.all()
        rankList = []
        rank = {}
        for rush in all_rushes:
            specific_rank_value = all_rankings.filter(
                rush__id=rush.id).aggregate(Sum('rank'))
            specific_rank_value = specific_rank_value['rank__sum']
            if specific_rank_value != None:
                number_of_rankings = all_rankings.filter(
                    rush__id=rush.id).count()
                average_rank = specific_rank_value / number_of_rankings
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
        return Comment.objects.filter(user__id=self.request.user.id)
