from django.shortcuts import render
from django.views import generic
from ranking.models import Ranking
from django.http import JsonResponse
from rest_framework import serializers
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from rushtracker.models import Rush
import json


class RankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ranking
        fields = ('id', 'rush', 'rank')


class createRank(generic.TemplateView):
    template_name = "ranking/create_rank.html"


class submitRank(generic.UpdateView):
    #ensure that rushID belongs to users organization
    def post(self, request, *args, **kwargs):
        stream = BytesIO(request.body)
        data = JSONParser().parse(stream)
        rank_object = RankSerializer(data=data)
        rank_object.is_valid(raise_exception=True)
        user = self.request.user
        qs = user.profile.ranking.all()
        rank_object.save()
        if not user.profile.ranking.filter(rush__id=rank_object.validated_data['rush'].id).exists():
        #querying data using [] and just calling it return two different things
        #second returns id associated with instance
        #accessing validated_data prevents any problems
            rank_data = rank_object.data
            user.profile.ranking.add(rank_data['id'])
            return JsonResponse({
                'success': True,
            })
        return JsonResponse({
            'success': False,
        })
