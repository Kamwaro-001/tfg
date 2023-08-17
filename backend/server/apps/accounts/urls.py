from django.urls import path, include
from .views import *


urlpatterns = [
    path("api/accounts/", include("djoser.urls")),
    path("api/accounts/", include("djoser.urls.jwt")),
]
