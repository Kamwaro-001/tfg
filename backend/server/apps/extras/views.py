from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *
from .models import *


class TreeInfoViewset(viewsets.ModelViewSet):
    queryset = TreeInfo.objects.all()
    serializer_class = TreeInfoSerializer


class ClassificationViewset(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer


class NotificationViewset(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer    
    queryset = Notifications.objects.all().order_by('-id')

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)

    def get_queryset(self):
        get_notif = Notifications.objects.all()
        for q in get_notif:
            q.save(update_fields=['time_sent'])
            
        return self.queryset.filter(username=self.request.user)


class FeedbackViewset(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
