from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response

from .models import CustomUser
from .serializers import *


class CustomRegisterView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer


class UserAPIView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class GenericUserAPIView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    lookup_field = "id"
