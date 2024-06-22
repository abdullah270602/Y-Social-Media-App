from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView # type: ignore
from . import api


urlpatterns = [
     path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
     path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
     path("signup/", api.signup, name="signup"),
     path("check-email-exists/", api.check_email_exists, name="check_email_exists"),
     path("check-username-exists/", api.check_username_exists, name="check_username_exists"),
     path("submit-username/", api.submit_username, name="submit_username"),
     path("verify-email/<uuid:token>", api.verify_email, name="verify_email"),
]