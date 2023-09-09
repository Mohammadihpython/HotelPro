from django.contrib.auth import authenticate
from rest_framework import serializers

from ..models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize CustomUser model.
    """

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "phone_number",
        )


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize registration requests and create a new user.
    """

    class Meta:
        model = CustomUser
        fields = ("id", "username", "phone_number", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        if CustomUser.objects.filter(phone_number=validated_data["phone_number"]).exists():

        return CustomUser.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer class to authenticate users with email and password.
    """

    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
