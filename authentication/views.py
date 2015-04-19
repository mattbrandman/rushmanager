from django.shortcuts import render
from django.views import generic
from authentication.forms import ChapterAdminForm, SingleUserCreationForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import get_user_model
import json
class SignUpFormView(generic.CreateView):
	template_name = 'authentication/register.html'
	form_class = ChapterAdminForm
	model = User
	def get_success_url(self):
		return reverse('rushtracker:index')
class AddSingleBrother(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
	model = User
	permission_required = 'authentication.chapter_admin'
	form_class = SingleUserCreationForm
	def get(self, request, *args, **kwargs):
		#TODO: this but in a better way perhaps in the urlconf
		return HttpResponseRedirect(reverse('rushtracker:index'))
	def form_invalid(self, form):
		return JsonResponse({
			'success':False,
			'errors': dict(form.errors.items()),
			})
	def form_valid(self, form):
		self.object = form.save()
		return JsonResponse({
			'success':True,
			'email': self.object.email
			})
	def get_form_kwargs(self):
		kwargs = super(AddSingleBrother, self).get_form_kwargs()
		kwargs['request'] = self.request
		return kwargs