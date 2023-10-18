from django.urls import path
from . import views

app_name = "room"


urlpatterns = [
    path(
        "suggestion", views.RoomSuggestionAPIView.as_view(), name="suggestion"
    )
]
