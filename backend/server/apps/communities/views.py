from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *


class CommunityViewset(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class MembersViewset(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = CommunityMembers.objects.all()
    serializer_class = MembersSerializer


class ActivitiesViewset(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = CommunityActivities.objects.all()
    serializer_class = ActivitiesSerializer
