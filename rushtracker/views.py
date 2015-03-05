from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from rushtracker.forms import DetailForm, CreateRushForm
from rushtracker.models import  Rush
from authentication.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate, login
from braces.views import LoginRequiredMixin

class IndexView(LoginRequiredMixin, generic.ListView):
	template_name = 'rushtracker/index.html'
	context_object_name = 'all_rushes'

	def get_queryset(self):
		return Rush.objects.filter(organization = self.request.user.profile.organization)

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
	def get_form_kwargs(self):
		kwargs = super(RushCreateView, self).get_form_kwargs()
		kwargs['request'] = self.request
		return kwargs
	def get_success_url(self):
		return reverse('rushtracker:index')

class RushDetailView(LoginRequiredMixin, generic.DetailView):

	model = Rush
	context_object_name = 'rush'

	def get_context_data(self, **kwargs):
	 	 context = super(RushDetailView, self).get_context_data(**kwargs)
	 	 context['rush_attendance'] = context['rush'].event_set.order_by('date')
	 	 return context
