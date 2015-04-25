from django.shortcuts import render
from django.views import generic
from ranking.models import Ranking
from django.http import JsonResponse
from rest_framework import serializers
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from rushtracker.models import Rush
import json

class createRank(generic.TemplateView):
    template_name = "ranking/create_rank.html"
