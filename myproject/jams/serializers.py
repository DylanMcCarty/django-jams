from .models import Users, Playlists
from rest_framework import serializers

class UsersSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

class PlaylistsSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Playlists
        fields = "__all__"
