from rest_framework.permissions import BasePermission
from django.utils import timezone
import datetime

class is_owner(BasePermission):
	def has_object_permission(self, request, view, obj):
		if obj.user == request.user or request.user.is_staff:
			return True
		return False

class morethanthree(BasePermission):
	def has_object_permission(self, request, view, obj):
		if obj.date >= datetime.date.today() + datetime.timedelta(days = 3):
			return True
		return False



