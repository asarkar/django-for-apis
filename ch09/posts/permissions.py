from django.views.generic import View
from rest_framework import permissions
from rest_framework.request import Request

from .models import Post


class IsAuthorOrReadOnly(permissions.BasePermission):
    # Only authors can edit or delete their posts
    def has_object_permission(self, request: Request, view: View, obj: Post) -> bool:
        # Read permissions are allowed to any request so we'll always
        # allow GET, HEAD, or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of a post
        return obj.author == request.user
