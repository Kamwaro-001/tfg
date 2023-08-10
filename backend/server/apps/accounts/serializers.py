from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from .models import *


class UserRegisterSerializer(RegisterSerializer):
    # email = serializers.EmailField(max_length=255)
    # username = serializers.CharField(max_length=255)
    # first_name = serializers.CharField(max_length=255)
    # last_name = serializers.CharField(max_length=255)
    # phone_number = serializers.CharField(max_length=255)
    # town = serializers.CharField(max_length=255)
    # county = serializers.CharField(max_length=255)

    # Define transaction.atomic to rollback the save operation in case of error
    # @transaction.atomic
    # def save(self, request):
    #     user = super().save(request)
    #     user.email = self.data.get('email')
    #     user.username = self.data.get('username')
    #     user.first_name = self.data.get('first_name')
    #     user.last_name = self.data.get('last_name')
    #     user.phone_number = self.data.get('phone_number')
    #     user.town = self.data.get('town')
    #     user.county = self.data.get('county')
    #     user.save()
    #     return user
    class Meta:
        model = CustomUser
        fields = ("email", "username", "first_name",)
        read_only_fields = ("email",)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "town",
            "county",
            "is_active",
        ]
