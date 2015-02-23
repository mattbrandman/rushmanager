from django.shortcuts import render
from django.views import generic
from authentication.forms import UserForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class SignUpFormView(generic.CreateView):
	template_name = 'authentication/register.html'
	form_class = UserForm
	model = User
	def get_success_url(self):
		return reverse('rushtracker:index')