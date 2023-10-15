from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views
app_name = "account"


urlpatterns = [
    path("register/", views.RegisterAPIView.as_view(), name="register"),
    path("login/", views.UserLoginAPIView.as_view(), name="login-user"),
    path(
        "changepassword/", views.ChangePasswordAPIView.as_view(), name="change-password"
    ),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("logout/", views.UserLogoutAPIView.as_view(), name="logout-user"),
    path("", views.UserAPIView.as_view(), name="user-info"),
]
