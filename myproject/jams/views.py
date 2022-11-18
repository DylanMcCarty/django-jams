from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from .models import Users, Playlists, Artist, Album, Song
from rest_framework.response import Response
from .serializers import UsersSerializer, PlaylistsSerializer, ArtistSerializer, AlbumSerializer, SongSerializer


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
    
    def post(self, request, format=None):
        data = request.data
        serializer = UsersSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message' : 'User created succesfully',
            'data' : serializer.data,
        }

        return response

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

class AlbumAPIView(APIView):
    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = AlbumSerializer(data)

        else:
            data = Album.objects.all()
            serializer = AlbumSerializer(data, many=True)

        return Response(serializer.data)  


class SongAPIView(APIView):
    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = SongSerializer(data)

        else:
            data = Song.objects.all()
            serializer = SongSerializer(data, many=True)

        return Response(serializer.data)  