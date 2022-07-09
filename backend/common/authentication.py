from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.settings import api_settings
from common.exceptions import TokenIsInvalidOrExpired, TokenIsRequired, TokenIsEmpty
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from common.choices import UserStatus

class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            raise TokenIsRequired()
        
        if len(header) == 0:
            raise TokenIsEmpty()

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)

        return self.get_user(validated_token), validated_token

    def get_validated_token(self, raw_token):
        for AuthToken in api_settings.AUTH_TOKEN_CLASSES:
            try:
                return AuthToken(raw_token)
            except TokenError:
                raise TokenIsInvalidOrExpired()


class CustomModelBackend(ModelBackend):
    def authenticate(self, request, email, password, **kwargs):
        user_model = get_user_model()
        try:
            user = user_model.objects.exclude(status=UserStatus.SUSPENDED).get(email=email)
        except user_model.DoesNotExist:
            return
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
