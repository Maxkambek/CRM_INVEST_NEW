from rest_framework import generics
from .models import Block, Floor, Room, AmountSkidki, RoomDetails
from .serializer import BlockSerializer, FloorSerializer, RoomSerializer, RoomSerializer2, AmountSkidkiSerializer, \
    RoomDetailUpdateSerializer


class RoomDetailUpdateAPIView(generics.UpdateAPIView):
    queryset = RoomDetails.objects.all()
    serializer_class = RoomDetailUpdateSerializer


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


class RoomDetailAPIView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer2


class SkidkiAPIView(generics.ListAPIView):
    queryset = AmountSkidki.objects.all()
    serializer_class = AmountSkidkiSerializer
