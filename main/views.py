from rest_framework import generics
from .models import Block, Floor, Room
from .serializer import BlockSerializer, FloorSerializer, RoomSerializer


class BlockListAPIView(generics.ListAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer


class FloorListAPIView(generics.ListAPIView):
    serializer_class = FloorSerializer

    def get_queryset(self):
        pk = self.request.GET.get('block_id')
        queryset = Floor.objects.filter(block_id=pk)
        return queryset


class RoomListAPIView(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        pk = self.request.GET.get('floor_id')
        queryset = Room.objects.filter(floor_id=pk)
        return queryset
