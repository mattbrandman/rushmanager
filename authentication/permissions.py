from rest_framework import permissions

class IsMineOrOwner(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		return obj.user == request.user or request.user.has_perm('chapter_admin')
