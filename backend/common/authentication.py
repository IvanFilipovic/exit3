from rest_framework.authentication import BaseAuthentication
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed

class BasicAPIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header != f"Basic {settings.BASIC_API_KEY}":
            raise AuthenticationFailed("Invalid or missing API Key")
        return (None, None)
