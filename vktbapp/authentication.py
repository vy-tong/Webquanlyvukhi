from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import usermod

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('HTTP_X_USERNAME')
        if not username:
            return None

        try:
            user = usermod.objects.get(username=username)
        except usermod.DoesNotExist:
            raise AuthenticationFailed('No such user')

        return (user, None) 