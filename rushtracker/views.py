from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from rushtracker.forms import UpdateForm, CreateRushForm
from rushtracker.models import  Rush
from comments.models import Comment
from authentication.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate, login
from braces.views import LoginRequiredMixin
from authentication.mixins import CorrectOrganizationMixin

class IndexView(LoginRequiredMixin, generic.ListView):
	template_name = 'rushtracker/index.html'
	context_object_name = 'all_rushes'
	def get_queryset(self):
		return Rush.tenant_objects.all()

class UpdateView(LoginRequiredMixin, CorrectOrganizationMixin, generic.UpdateView):
	template_name = 'rushtracker/update.html'
	form_class = UpdateForm
	model = Rush
	context_object_name='rush'
	def get_success_url(self):
		return reverse('rushtracker:index')
	def dispatch(self, request, *args, **kwargs):
		self.organization = get_object_or_404(Rush, pk=kwargs['pk']).organization
		return super(UpdateView, self).dispatch(request, *args, **kwargs)

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
	 	 if context['rush'].comment_set.all():
		 	context['comments'] = reversed(context['rush'].comment_set.order_by('-created_at')[:5])
		 else:
		 	context['comments'] = False
		 	
 	 	 return context
