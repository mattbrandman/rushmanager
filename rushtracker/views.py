from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from rushtracker.forms import DetailForm, UserForm, UserProfileForm
from rushtracker.models import Brother, Rush, UserProfile
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
class IndexView(generic.ListView):
	template_name = 'rushtracker/index.html'
	context_object_name = 'all_rushes'

	def get_queryset(self):
		return Rush.objects.all()

class UpdateView(generic.UpdateView):
	#model is used for indicate what to pass to the detail view
	#that it can use to pull data
	template_name = 'rushtracker/update.html'
	model = Rush
	form_class = DetailForm

	def get_success_url(self):
		return reverse('rushtracker:index')


class SignUpFormView(generic.CreateView):
	template_name = 'rushtracker/register.html'
	form_class = UserForm
	model = User

	def form_valid(self, form):
		UserProfileTemp = UserProfile()
		UserProfileTemp.user = form.save(commit=False)
		UserProfileTemp.save()
		return super(SignUpFormView, self).form_valid(form)
	def get_success_url(self):
		return reverse('rushtracker:index')