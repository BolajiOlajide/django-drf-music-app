from rest_framework.serializers import ModelSerializer
from music.models import Song


class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = ("title", "artist")
