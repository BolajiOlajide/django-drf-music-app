from rest_framework.generics import ListAPIView
from music.models import Song
from music.serializers import SongSerializer


class ListSongsView(ListAPIView):
    """
    Provides a get method handler.
    """

    queryset = Song.objects.all()
    serializer_class = SongSerializer
