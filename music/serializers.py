from rest_framework.serializers import ModelSerializer, Serializer, CharField
from music.models import Song


class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = ("title", "artist")


class TokenSerializer(Serializer):
    """
    This serializer serializes the token data
    """

    token = CharField(max_length=255)
