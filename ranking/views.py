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
    #TODO: perhaps this should be done in DRF using the same
    #request pass through used for user
    def post(self, request, *args, **kwargs):
        #be able to turn it into string
        #handles request.body or string (mainly for ensuring either works)
        stream = BytesIO(request.body)
        #turns it into a string and converts it to json 
        #Python 3 would error if we just stried to go straight to Json
        #from request,body which is a byte string
        data = JSONParser().parse(stream)
        rank_object = RankSerializer(data=data)
        rank_object.is_valid(raise_exception=True)
        user = self.request.user
        qs = user.profile.ranking.all()
        if not Rush.tenant_objects.filter(id=rank_object.validated_data['rush'].id).exists():
            return JsonResponse({
                'error': 'You are trying to rank a non-existant rush'
                })

        if not user.profile.ranking.filter(rush__id=rank_object.validated_data['rush'].id).exists():
        #querying data using [] and just calling it return two different things
        #second returns id associated with instance
        #accessing validated_data prevents any problems
            rank_object.save()
            rank_data = rank_object.data
            user.profile.ranking.add(rank_data['id'])
            return JsonResponse({
                'success': True,
            })
        return JsonResponse({
            'success': False,
        })