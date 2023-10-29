from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .. import models
from . import serializers
from ..tasks import send_sms_code
import random


user = get_user_model()


class UserLoginAPIView(GenericAPIView):
    queryset = models.CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        user = serializer.validated_data
        serializer = serializers.UserSerializer(user)
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["token"] = {"refresh": str(token), "access": str(token.access_token)}  # type: ignore
        return Response(data, status=status.HTTP_201_CREATED)


class UserLogoutAPIView(GenericAPIView):
    queryset = models.CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_206_PARTIAL_CONTENT)
        except Exception as e:
            return Response({"msg": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user


class RegisterAPIView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.OTPRequestSerializer
        return serializers.OTPVerifiedRequestSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.query_params)
        if not serializer.is_valid(raise_exception=True):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        data = serializer.validated_data
        otp_code = "".join(str(random.randint(0, 9)) for _ in range(6))

        try:
            data["code"] = otp_code
            models.UserOTP.objects.generate(data)
            send_sms_code.delay(data["phone_number"], otp_code)

            return Response(
                data={
                    "msg": "code send to user",
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"msg": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(
                {"msg": "data is invalid"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        data = serializer.validated_data

        if not models.UserOTP.objects.is_valid(
            phone_number=data["phone_number"],
            code=data.pop("code"),
        ):
            return Response(
                {"msg": "wrong code or phone_number"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if models.CustomUser.objects.filter(phone_number=data["phone_number"]).exists():
            return Response(
                data={"msg": "user already exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        "create user and it s tokens and return them as Response"

        try:
            return self._create_user(data)
        except Exception as e:
            return Response(
                data={"msg": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def _create_user(self, data):
        user = models.CustomUser(phone_number=data["phone_number"], username=data["username"])
        user.set_password(data["password"])
        user.save()
        token = RefreshToken.for_user(user)
        data["refresh_token"] = str(token)

        data["access_token"] = str(token.access_token)

        serializer = serializers.OTPVerifiedResponseSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            "internal error in create user or token",
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


class ChangePasswordAPIView(UpdateAPIView):
    queryset = models.CustomUser.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ChangePasswordSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.user = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if not self.user.check_password(serializer.data.get("old_password")):
                return Response(
                    {"msg": "wrong old password"}, status=status.HTTP_400_BAD_REQUEST
                )
            user.set_password(serializer.data.get("new_password"))  # type: ignore
            return Response(
                {"detail": "Password updated successfully."}, status=status.HTTP_200_OK
            )
