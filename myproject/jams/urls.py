from django.urls import path 
from .views import UsersAPIView, PlaylistsAPIView

urlpatterns = [
    path('users/', UsersAPIView.as_view()),
    path('users/<str:pk>/', UsersAPIView.as_view()),
    path('playlists/', PlaylistsAPIView.as_view())
]