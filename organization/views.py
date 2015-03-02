from django.shortcuts import render
from django.views import generic
from braces.views import LoginRequiredMixin
from rushtracker.models import Rush
from organization.models import Organization
from organization.forms import CreateOrganizationForm
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.contrib.auth.models import User
class OrganizationCreateView( generic.CreateView):
	template_name = 'organization/create_organization.html'
	model = Organization
	form_class = CreateOrganizationForm
	def get_success_url(self):
		return reverse('organization:organization_home')

class OrganizationHome(generic.TemplateView):
	template_name = 'organization/organization_home.html'
	def get(self, request, *args, **kwargs):
		user = self.request.user.profile.organization
		return super(OrganizationHome, self).get(self, request, *args, **kwargs)
	def get_context_data(self, **kwargs):
		organization = self.request.user.profile.organization
		context = super(OrganizationHome, self).get_context_data(**kwargs)
		context['organization'] = organization 
		return context 
