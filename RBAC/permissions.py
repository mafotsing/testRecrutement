from rest_framework import permissions

class IsMyPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        if user.is_my:
            if user.has_perm('client.add_client'):
                 return True
            if user.has_perm('client.change_client'):
                 return True
            if user.has_perm('client.delete_client'):
                 return True
            if user.has_perm('client.views_client'):
                 return True
            return False