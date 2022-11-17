from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from .models import Users, Playlists, Artist
from rest_framework.response import Response
from .serializers import UsersSerializer, PlaylistsSerializer, ArtistSerializer


class UsersAPIView(APIView):
    def get_object(self, pk):
        try:
            return Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = UsersSerializer(data)

        else:
            data = Users.objects.all()
            serializer = UsersSerializer(data, many=True)

        return Response(serializer.data)  
    

class PlaylistsAPIView(APIView):
    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = PlaylistsSerializer(data)

        else:
            data = Playlists.objects.all()
            serializer = PlaylistsSerializer(data, many=True)
        return Response(serializer.data)


class ArtistAPIView(APIView):
    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = ArtistSerializer(data)

        else:
            data = Artist.objects.all()
            serializer = ArtistSerializer(data, many=True)
        return Response(serializer.data)

