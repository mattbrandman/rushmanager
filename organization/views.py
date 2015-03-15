from django.shortcuts import render
from django.views import generic
from braces.views import LoginRequiredMixin
from rushtracker.models import Rush
from organization.models import Organization
from organization.forms import CreateOrganizationForm
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.contrib.auth.models import User

class OrganizationOverview(generic.DetailView):
	template_name='organization/overview.html'
	context_object_name='organization'
	model = Organization
	def get_object(self):
		return self.request.user.profile.organization