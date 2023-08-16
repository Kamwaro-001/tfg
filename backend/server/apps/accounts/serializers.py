from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from .models import *


class UserRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=False)
    town = serializers.CharField(required=False)
    county = serializers.CharField(required=False)

    def get_cleaned_data(self):
        super(UserRegisterSerializer, self).get_cleaned_data()

        return {
            "password": self.validated_data.get("password", ""),
            "email": self.validated_data.get("email", ""),
            "username": self.validated_data.get("username", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "town": self.validated_data.get("town", ""),
            "county": self.validated_data.get("county", ""),
        }

    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.email = self.data.get("email")
        user.username = self.data.get("username")
        user.first_name = self.data.get("first_name")
        user.last_name = self.data.get("last_name")
        user.phone_number = self.data.get("phone_number")
        user.town = self.data.get("town")
        user.county = self.data.get("county")
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "email",
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "town",
            "county",
            "password",
        ]
