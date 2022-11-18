from .models import Users, Playlists, Artist, Album, Song
from rest_framework import serializers

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

class PlaylistsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Playlists
        fields = "__all__"
        depth=1


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = "__all__"

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = "__all__"

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = "__all__"
        depth=1
