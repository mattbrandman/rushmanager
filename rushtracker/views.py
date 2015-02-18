from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from rushtracker.forms import DetailForm, UserForm, UserProfileForm, CreateRushForm
from rushtracker.models import Brother, Rush, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate, login
from django.contrib.auth.forms import AuthenticationForm


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
		UserProfileTemp = UserProfileForm()
		UserProfileObject = UserProfileTemp.save(commit=False)

		#holds the return value after the save 
		#uses the fact that self.object is assigned to the created user
		#to access that userId and assign it to a user profile
		returnHolder = super(SignUpFormView, self).form_valid(form)
		#The Super call turns self.object into a User Object Instance 
		#which is then used to register the user instantly and create a profile for them
		user = self.object
		UserProfileObject.user = user
		UserProfileObject.save()
		user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password1'])
		if user is not None:
			login(self.request, user)
			print("sucess")

		return returnHolder

	def get_success_url(self):
		return reverse('rushtracker:index')

class RushCreateView(generic.CreateView):
	template_name = 'rushtracker/create_rush.html'
	form_class = CreateRushForm
	model = Rush
	def get_success_url(self):
		return reverse('rushtracker:index')
