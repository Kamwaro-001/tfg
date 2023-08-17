from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register("plant", TreeInfoViewset, basename="plant")
router.register("classes", ClassificationViewset, basename="classes")
router.register("notifications", NotificationViewset, basename="notifications")
router.register("feedback", FeedbackViewset, basename="feedback")

urlpatterns = [
    path("", include(router.urls)),
]
