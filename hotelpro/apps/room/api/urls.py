from django.urls import path
from . import views

app_name = "room"


urlpatterns = [
    path(
        "room_suggestion", views.RoomSuggestionAPIView.as_view(), name="room-suggestion"
    )
]
