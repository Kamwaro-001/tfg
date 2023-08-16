from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register("users", UserAPIView, basename="users")


urlpatterns = [
    path("", include("djoser.urls")),
    path("", include("djoser.urls.jwt")),
    # path("", include("dj_rest_auth.auth_token")),
    # path('register/', include('dj_rest_auth.registration.urls')),
    # path('', include(router.urls))
]
