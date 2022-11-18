from django.urls import path 
from .views import UsersAPIView, PlaylistsAPIView, ArtistAPIView, AlbumAPIView, SongAPIView

urlpatterns = [
    path('users/', UsersAPIView.as_view()),
    path('users/<str:pk>/', UsersAPIView.as_view()),
    path('playlists/', PlaylistsAPIView.as_view()),
    path('artist/', ArtistAPIView.as_view()),
    path('album/', AlbumAPIView.as_view()),
    path('album/<str:pk>/', AlbumAPIView.as_view()),
    path('song/', SongAPIView.as_view())
]
