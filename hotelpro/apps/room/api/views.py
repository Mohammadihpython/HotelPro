from django.views.defaults import permission_denied
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import viewsets
from ..models import Room
from .serializers import RoomSerializer
from ..room_suggestion_ml import RoomSuggestionModel
from rest_framework.permissions import IsAuthenticated,IsAdminUser


class RoomSuggestionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        room_preferences = request.data

        model = RoomSuggestionModel()

        # Train the machine learning model
        model.train()

        # Save the trained model
        model.save_model(".model.pkl")

        # Load the trained model
        model.load_model(".model.pkl")

        # Make room suggestions
        suggested_room_type = model.predict_suggested_room(room_preferences)

        # Get the suggested room details from the database
        room = Room.objects.filter(room_type=suggested_room_type).first()

        # Serialize the room details
        serializer = RoomSerializer(room)

        return Response(serializer.data)


class CreateViewAPI(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = RoomSerializer


class RoomViewSets(viewsets.ModelViewSet):
    serializer_class = RoomSerializer

    def get_permissions(self):

        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


