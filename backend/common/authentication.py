from rest_framework.authentication import BaseAuthentication
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
from django.utils.crypto import constant_time_compare

class BasicAPIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization', '')

        if not auth_header.startswith('Basic '):
            raise AuthenticationFailed("Invalid authorization header format")

        provided_key = auth_header.replace('Basic ', '')
        expected_key = settings.BASIC_API_KEY or ''

        # Use constant_time_compare to prevent timing attacks
        if not expected_key or not constant_time_compare(provided_key, expected_key):
            raise AuthenticationFailed("Invalid or missing API Key")

        return (None, None)
