from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
# from django.contrib.auth import get_user_model

# User = get_user_model()


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        # model = User
        fields = ("id", "email", "username", "first_name", "last_name", "phone_number", "town", "county", "password")
        # fields = ("id", "email", "username", "first_name", "last_name", "password")