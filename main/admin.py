from django.contrib import admin
from .models import Block, Floor, Room, RoomDetails, AmountSkidki


class RoomDetailAdmin(admin.StackedInline):
    model = RoomDetails
    extra = 0


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    pass


@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ['name','block']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomDetailAdmin]
    list_display = ['floor','room_number']
    list_filter = ['floor']