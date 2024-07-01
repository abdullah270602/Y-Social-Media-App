from django.urls import  path
from . import api

urlpatterns = [
    path("create/", api.create_post, name="create_post"),
    path("", api.get_posts, name="posts"),
]
