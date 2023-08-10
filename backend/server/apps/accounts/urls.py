from django.urls import path, include
from rest_framework import routers

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path('register/', include('dj_rest_auth.registration.urls'))
]
