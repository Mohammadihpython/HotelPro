import random
from rest_framework import serializers
from ..models import CustomUser, UserOTP
from ..tasks import send_sms_code, verify_sms

from django.core.validators import RegexValidator


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


phone_regex = RegexValidator(
    regex=r"^09\d{9}$",
    message="Phone number must be entered in the format: "
    "'09xxxxxxxxx'. Up to 11 digits allowed.",
)


class OTPRequestSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        max_length=11, validators=[phone_regex], required=True
    )

    def validate(self, data):
        if CustomUser.objects.filter(phone_number=data["phone_number"]).exists():
            raise serializers.ValidationError("user already exists")
        else:
            return data


class OtpResponseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["phone_number"]


class OTPVerifiedRequestSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        max_length=11, validators=[phone_regex], required=True
    )
    password = serializers.CharField(max_length=50, required=True)
    code = serializers.CharField(max_length=6, required=True)
    username = serializers.CharField(max_length=100, required=True)


class OTPVerifiedResponseSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(max_length=256, required=True)
    access_token = serializers.CharField(max_length=256, required=True)
    username = serializers.CharField(max_length=100, required=True)
    phone_number = serializers.CharField(max_length=11, required=True)


class UserLoginSerializer(serializers.ModelSerializer):
    """
    Serializer class to authenticate users with email and password.
    """

    class Meta:
        model = CustomUser
        fields = ("phone_number", "password")

    def validate(self, data: object) -> object:
        phone = data.get("phone_number")
        password = data.get("password")
        user = (
            CustomUser.objects.filter(phone_number=phone)
            .select_related("password")
            .first()
        )
        if user and user.check_password(password):
            return data
        else:
            raise serializers.ValidationError("password or phone is wrong")


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)
