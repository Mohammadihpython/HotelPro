from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("hotelpro.apps.account.api.urls", namespace="account")),
]
