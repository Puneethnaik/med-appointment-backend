from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsCreationOrIsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'POST':
            return True
        else:
            return False