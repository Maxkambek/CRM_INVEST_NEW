from django.contrib import admin
from .models import Block, Floor, Room, RoomDetails, AmountSkidki


@admin.register(AmountSkidki)
class AmountSkidkiAdmin(admin.ModelAdmin):
    pass


class RoomDetailAdmin(admin.StackedInline):
    model = RoomDetails
    extra = 1


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    pass


@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomDetailAdmin]
