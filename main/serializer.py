from .models import Block, Floor, Room, RoomDetails, AmountSkidki
from rest_framework import serializers


class AmountSkidkiSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmountSkidki
        fields = '__all__'


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


class RoomDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomDetails
        fields = ['count_rooms','full_area','id','terrace_area', 'image_1','image_2','client_name','price_0','price_30','price_50','price_100','terrace_price_0','terrace_price_30','terrace_price_50','terrace_price_100','room']


class RoomSerializer2(serializers.ModelSerializer):
    room_details = RoomDetailsSerializer(many=True)

    class Meta:
        model = Room
        fields = ['id', 'room_number', 'status_room', 'room_details']
