from rest_framework import serializers

from .models import *


class TreeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreeInfo
        read_only_fields = ("username",)
        fields = "__all__"


class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = "__all__"


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        read_only_fields = (
            "when",
            "time_sent",
        )
        fields = "__all__"


class FeedbackSerializer(serializers.Serializer):
    class Meta:
        model = Feedback
        read_only_fields = ("date",)
        fields = "__all__"
