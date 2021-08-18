from rest_framework.permissions import BasePermission


def user_type(user):
    if user.is_staff == True and user.is_superuser == False:
        return 'critic'

    if user.is_staff == True and user.is_superuser == True:
        return 'admin'


class MoviePermissions(BasePermission):
    def has_permission(self, request, view):
        user = user_type(request.user)

        if request.method == 'GET':
            return True

        if request.method == 'POST' or request.method == 'DELETE':
            return True if user == 'admin' else False


class ReviewPermissions(BasePermission):
    def has_permission(self, request, view):
        user = user_type(request.user)

        if request.method == 'GET':
            return True

        if request.method == 'POST':
            # return True if user == 'critic' else False
            return True
