from django.shortcuts import render
from django.views import generic
class rank(generic.TemplateView):
	template_name = "ranking/create_rank.html"
