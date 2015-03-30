from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from authentication.forms import SingleUserCreationForm
from django.db.models import Q
from django.contrib.auth import get_user_model

class IndexView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
	template_name="chaptermanagement/user_index.html"
	context_object_name = 'all_users'
	permission_required = "authentication.chapter_admin"

	def get_queryset(self):
		return get_user_model().tenant_objects.all()
		
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['SingleUserCreationForm'] = SingleUserCreationForm
		return context