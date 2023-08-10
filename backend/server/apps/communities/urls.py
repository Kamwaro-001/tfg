from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register("communities", CommunityViewset, basename="communities")
router.register("members", MembersViewset, basename="members")
router.register("activities", ActivitiesViewset, basename="activities")

urlpatterns = [path("api/", include(router.urls))]
