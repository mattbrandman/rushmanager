from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from rushtracker.forms import DetailForm, CreateRushForm
from rushtracker.models import  Rush, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate, login
from braces.views import LoginRequiredMixin

class IndexView(LoginRequiredMixin, generic.ListView):
	template_name = 'rushtracker/index.html'
	context_object_name = 'all_rushes'

	def get_queryset(self):
		return Rush.objects.all()

class UpdateView(LoginRequiredMixin, generic.UpdateView):
	#model is used for indicate what to pass to the detail view
	#that it can use to pull data
	template_name = 'rushtracker/update.html'
	model = Rush
	form_class = DetailForm

	def get_success_url(self):
		return reverse('rushtracker:index')

class RushCreateView(LoginRequiredMixin, generic.CreateView):
	template_name = 'rushtracker/create_rush.html'
	form_class = CreateRushForm
	model = Rush
	def get_success_url(self):
		return reverse('rushtracker:index')
