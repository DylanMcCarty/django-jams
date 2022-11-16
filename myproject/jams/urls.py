from django.urls import path 
from .views import UsersAPIView

urlpatterns = [
    path('users/', UsersAPIView.as_view()),
    path('users/<str:pk>/', UsersAPIView.as_view())
]