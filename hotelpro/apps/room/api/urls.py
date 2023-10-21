from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = "room"


router = DefaultRouter()
router.register(r'rooms', views.RoomViewSets, basename='room')

urlpatterns = [
    path(
        "suggestion", views.RoomSuggestionAPIView.as_view(), name="suggestion"
    )
] + router.urls
