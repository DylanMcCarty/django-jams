from .models import Users, Playlists
from rest_framework import serializers

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

class PlaylistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlists
        fields = "__all__"
