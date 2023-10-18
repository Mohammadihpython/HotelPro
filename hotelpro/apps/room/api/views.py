from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Room
from .serializers import RoomSerializer
from ..room_suggestion_ml import RoomSuggestionModel
from rest_framework.permissions import IsAuthenticated


class RoomSuggestionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        room_preferences = request.data

        model = RoomSuggestionModel()

        # Train the machine learning model
        model.train()

        # Save the trained model
        model.save_model("path_to_serialized_model/model.pkl")

        # Load the trained model
        model.load_model("path_to_serialized_model/model.pkl")

        # Make room suggestions
        suggested_room_type = model.predict_suggested_room(room_preferences)

        # Get the suggested room details from the database
        room = Room.objects.filter(room_type=suggested_room_type).first()

        # Serialize the room details
        serializer = RoomSerializer(room)

        return Response(serializer.data)
