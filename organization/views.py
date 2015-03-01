from django.shortcuts import render
from django.views import generic
from braces.views import LoginRequiredMixin
from rushtracker.models import Rush
from organization.models import Organization
from organization.forms import CreateOrganizationForm
from django.core.urlresolvers import reverse
from django.http import JsonResponse
class OrganizationCreateView( generic.CreateView):
	template_name = 'organization/create_organization.html'
	model = Organization
	form_class = CreateOrganizationForm
	def get_success_url(self):
		return reverse('organization:organization_home')

class OrganizationHome(generic.DetailView):
	template_name = 'organization/organization_home.html'
	model = Organization
	def __init__(self, **kwargs):
		super(OrganizationHome, self).__init__(**kwargs)
		self.request.user.UserProfile.organization.chapter_name

