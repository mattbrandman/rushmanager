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


class createRank(generic.TemplateView):
    template_name = "ranking/create_rank.html"


class submitRank(generic.UpdateView):

    def post(self, request, *args, **kwargs):
        stream = BytesIO(request.body)
        data = JSONParser().parse(stream)
        ms = RankSerializer(data=data)
        ms.is_valid()
        profile = self.request.user.profile
        if profile.ranking.filter(rush__id=ms.data['rush']).exists():
            ms.save()
            print ms.data
            profile.ranking.add(ms.data['id'])
            return JsonResponse({
                'success': True,
            })
        return JsonResponse({
            'success': False,
        })
