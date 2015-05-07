from tastypie.resources import ModelResource
from django.contrib.auth import get_user_model
from rushtracker.models import Rush
from rushperiod.models import RushPeriod
from comments.models import Comment
from ranking.models import Ranking
from organization.models import Organization
from django.contrib.auth.models import Permission
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from authentication.models import UserProfile
from events.models import Event
from tastypie import fields


class UserResource(ModelResource):
	class Meta:
		queryset = get_user_model().tenant_objects.all()
		allowed_methods = ['get']
		fields = ('email',)


class RushResource(ModelResource):
	primary_contact = fields.ForeignKey(UserResource, 'primary_contact', null=True, full=True)
	class Meta:
		queryset = Rush.tenant_objects.all()
		fields = ('first_name', 'primary_contact')