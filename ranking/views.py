from django.shortcuts import render
from django.views import generic
from django_extensions import db.fields.json
class rank(generic.TemplateView):
	template_name = "create_rank.html"
