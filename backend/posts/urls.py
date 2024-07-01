from django.urls import  path
from . import api

urlpatterns = [
    path("create/", api.create_post, name="create_post"),
    path("", api.get_posts, name="posts"),
    path('toggle_post_like/<uuid:postId>', api.toggle_post_like, name='toggle_post_like'),
    path('toggle_post_bookmark/<uuid:postId>', api.toggle_post_bookmark, name='toggle_post_bookmark'),


]
