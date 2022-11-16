from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from .models import Users
from rest_framework.response import Response
from .serializers import UsersSerilizer


class UsersAPIView(APIView):
    def get_object(self, pk):
        try:
            return Users.object.get(pk=pk)
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = UsersSerilizer(data)

        else:
            data = Users.objects.all()
            serializer = UsersSerilizer(data, many=True)

        return Response(serializer.data)  

