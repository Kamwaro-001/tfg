from rest_framework import serializers

from .models import *


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        read_only_fields = ("id", "verif_code", "date_created")
        fields = "__all__"


class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityMembers
        # TODO add the read only fields after the necessary requirements are met
        read_only_fields = ("id", "date_joined")
        fields = "__all__"


class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityActivities
        read_only_fields = "id"
        fields = "__all__"
