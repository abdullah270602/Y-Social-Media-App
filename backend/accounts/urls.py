from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView # type: ignore
from . import api


urlpatterns = [
     path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
     path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
     path("signup/", api.signup, name="signup"),
     path("check-email-exists/", api.check_email_exists, name="check_email_exists"),
     path("check-username-exists/", api.check_username_exists, name="check_username_exists"),
     path("verify-email/<uuid:token>", api.verify_email, name="verify_email"),
     path("get-user-info/", api.get_user_info, name="get_user_info"),
     path("follow/<str:username>", api.follow_request, name="follow"),
     path("unfollow/<str:username>", api.unfollow_request, name="unfollow"),
     path("check-follow-relationship/<str:username>", api.check_follow_relationship, name="check_follow_relationship"),    path("get-user-following-and-followers-count/<uuid:id>", api.get_user_following_and_followers_count, name="get_user_following_and_followers_count"),
     path("get-user-following-and-followers-count/<str:username>", api.get_user_following_and_followers_count, name="get_user_following_and_followers_count"),

]