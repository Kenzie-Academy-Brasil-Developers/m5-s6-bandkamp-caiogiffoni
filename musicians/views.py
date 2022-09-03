from albums.models import Album
from albums.serializers import AlbumSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView, Response, status
from songs.models import Song
from songs.serializers import SongSerializer

import musicians

from .models import Musician
from .serializers import MusicianSerializer


class MusicianView(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
    lookup_url_kwarg = "musician_id"


class MusicianAlbumView(generics.ListCreateAPIView):
    serializer_class = AlbumSerializer

    def perform_create(self, serializer):
        musician = get_object_or_404(Musician, pk=self.kwargs["musician_id"])
        serializer.save(musician=musician)

    def get_queryset(self):
        musician = get_object_or_404(Musician, pk=self.kwargs["musician_id"])
        return Album.objects.filter(musician_id=self.kwargs["musician_id"])


class MusicianAlbumSongsView(generics.ListCreateAPIView):
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        musician = get_object_or_404(Musician, pk=self.kwargs["musician_id"])
        album = get_object_or_404(Album, pk=self.kwargs["album_id"])
        serializer.save(album=album)

    def get_queryset(self):
        musician = get_object_or_404(Musician, pk=self.kwargs["musician_id"])
        album = get_object_or_404(Album, pk=self.kwargs["album_id"])
        return Song.objects.filter(album_id=self.kwargs["album_id"])
