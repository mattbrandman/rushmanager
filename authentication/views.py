from django.shortcuts import render
from django.views import generic
from authentication.forms import ChapterAdminForm, SingleUserCreationForm, ChangePasswordForm, UserUpdateNameForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import get_user_model
from braces.views import UserFormKwargsMixin
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


class ChangePassword(LoginRequiredMixin, UserFormKwargsMixin, generic.UpdateView):
	model = User
	form_class = ChangePasswordForm
	template_name = 'authentication/change_password.html'

	def get_form_kwargs(self):
		kwargs = super(ChangePassword, self).get_form_kwargs()
		kwargs['request'] = self.request
		return kwargs

	def get_success_url(self):
		return reverse('rushtracker:index')

	def get_object(self, queryset=None):
		return self.request.user


class UserProfile(LoginRequiredMixin, generic.DetailView):
	model = User
	context_object_name = 'user'
	template_name = 'authentication/user_profile.html'

	def get_object(self):
		return self.request.user


class UserUpdateNameView(UpdateView):
	model = get_user_model()
	success_url = '/'
	form_class = UserUpdateNameForm

	def get_form_kwargs(self):
		kwargs= super(UserUpdateNameView, self).get_form_kwargs()
		kwargs['request'] = self.request
		return kwargs
