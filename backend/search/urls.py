
from django.urls import include, path
from . import api

urlpatterns = [
    path('', api.search, name='search'),
]
