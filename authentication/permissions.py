from rest_framework import permissions

class SameOrganizationPermission(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.organization == request.user.organization