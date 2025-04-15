from rest_framework.permissions import BasePermission, IsAdminUser

SUPER_ADMIN=1
ADMIN=2

def IsAuthenticated(request):
        return bool(request.user and request.request.is_authenticated)

def SuperAdminLevel(request):
     return bool(IsAuthenticated(request) and request.user.is_superuser)

def AdminLevel(self, request):
    #  return bool(IsAuthenticated(request) and request.user.role in [SUPER_ADMIN, ADMIN])
    return bool(IsAdminUser(request) or request.user.is_superuser)

def isOwner(self, request):
        if str(request.user.id) == str(request.data.get('user')):
             return True
        elif len(request.data)==0 and len(request.POST)==0:
             return True
        return False

class bookPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list']:
            return True
        elif view.action == 'retrieve':
            return isOwner(request)
        elif view.action in ['create', 'update']:
            return IsAuthenticated(request)
        elif view.action == 'partial_update':
            return IsAuthenticated(request)
        elif view.action == 'destroy':
            return AdminLevel(request)
        
