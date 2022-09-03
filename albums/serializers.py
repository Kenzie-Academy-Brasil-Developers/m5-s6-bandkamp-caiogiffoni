from dataclasses import field

from rest_framework import serializers

from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["id", "name", "musician_id"]
        read_only_fields = ["musician_id"]
