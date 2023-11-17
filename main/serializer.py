from .models import Block, Floor, Room
from rest_framework import serializers


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['id', 'name']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room_number', 'status_room']


class FloorSerializer(serializers.ModelSerializer):
    floor_rooms = RoomSerializer(many=True)

    class Meta:
        model = Floor
        fields = ['id', 'name', 'block', 'floor_rooms']


