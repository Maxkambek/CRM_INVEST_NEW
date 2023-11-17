from . import views
from django.urls import path

urlpatterns = [
    path('block/', views.BlockListAPIView.as_view()),
    path('floor/', views.FloorListAPIView.as_view()),
    path('room/', views.RoomListAPIView.as_view())
]
