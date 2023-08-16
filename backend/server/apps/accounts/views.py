from django.shortcuts import render
from rest_framework.views import APIView

# from rest_framework import generics
# from rest_framework.mixins import *
from rest_framework import viewsets
# from rest_auth.registration.views import RegisterView
from dj_rest_auth.registration.views import RegisterView
from rest_framework.response import Response

from .models import CustomUser
from .serializers import *


class CustomRegisterView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer


# class UserAPIView(APIView):
#     @staticmethod
#     def get(request):
#         users = CustomUser.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
      
class UserAPIView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


# class GenericUserAPIView(generics.GenericAPIView, ListModelMixin, CreateModelMixin, UpdateModelMixin, Re)
class GenericUserAPIView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    lookup_field = "id"