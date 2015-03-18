from django.shortcuts import render
from django.views import generic
from braces.views import LoginRequiredMixin
from rushtracker.models import Rush
from organization.models import Organization
from organization.forms import CreateOrganizationForm, UpdateActiveRushPeriodForm
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.contrib.auth.models import User
from rushperiod.models import RushPeriod
from authentication.mixins import CorrectOrganizationMixin
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.http import JsonResponse


class OrganizationOverview(generic.DetailView):
	template_name='organization/overview.html'
	context_object_name='organization'
	model = Organization
	def get_object(self):
		return self.request.user.profile.organization

	def get_context_data(self, **kwargs):
		context = super(OrganizationOverview, self).get_context_data(**kwargs)
		context['RushPeriodForm'] = UpdateActiveRushPeriodForm(initial={'active_rush_period': self.request.user.profile.organization.active_rush_period})
		context['RushPeriodForm'].fields['active_rush_period'].queryset = RushPeriod.objects.filter(organization = self.request.user.profile.organization)
		return context
class SetActiveRushPeriod(CorrectOrganizationMixin, generic.UpdateView):
	model = Organization
	form_class = UpdateActiveRushPeriodForm
	def dispatch(self, request, *args, **kwargs):
		self.organization = get_object_or_404(RushPeriod, pk=request.POST['active_rush_period']).organization
		return super(SetActiveRushPeriod, self).dispatch(request, *args, **kwargs)

	def get_object(self):
		return self.request.user.profile.organization

	def form_valid(self, form):
		print "yes"
		response = super(SetActiveRushPeriod, self).form_valid(form)
		data = {
			'success':'True'
		}
		return JsonResponse(data)
	def form_invalid(self, form): 
		print "no"
		super(SetActiveRushPeriod, self).form_valid(form)
		return JsonResponse(form.errors, status=400)
	def get_success_url(self):
		return reverse('rushtracker:index')