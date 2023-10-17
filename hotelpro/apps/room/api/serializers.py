from django.forms import fields
from rest_framework.serializers import ModelSerializer
from ..models import Room, Media
from rest_framework import serializers


class MediaSerializer(ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ["alt_text", "is_default", "image_url"]

    def get_image_url(self, obj):
        return self.context["request"].build_absolute_uri(obj.image.url)


class RoomSerializer(ModelSerializer):
    images = MediaSerializer(source="media_room", many=True, read_only=True)

    class Meta:
        model = Room
        exclude = ["created_at", "updated_at"]
