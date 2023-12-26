from django.db import models


class Block(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Floor(models.Model):
    name = models.CharField(max_length=1234)
    block = models.ForeignKey(Block, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.block.name} {self.name}'


STATUS = (
    ('пустой', 'пустой'),
    ('бронирование', 'бронирование'),
    ('продано', 'продано'),
    ('не_продаже', 'не_продаже')
)


class Room(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='floor_rooms')
    room_number = models.CharField(max_length=123)
    status_room = models.CharField(choices=STATUS, default='пустой', max_length=123)

    def __str__(self):
        return self.room_number


class AmountSkidki(models.Model):
    percentage = models.PositiveIntegerField(default=5)

    def __str__(self):
        return f'{self.percentage}'


class RoomDetails(models.Model):
    count_rooms = models.CharField(max_length=12)
    full_area = models.FloatField(default=0)
    terrace_area = models.FloatField(default=0)
    image_1 = models.ImageField(upload_to='images/')
    image_2 = models.ImageField(upload_to='images/')
    client_name = models.CharField(max_length=123, null=True, blank=True)
    price_30 = models.PositiveIntegerField(default=0)
    price_50 = models.PositiveIntegerField(default=0)
    price_100 = models.PositiveIntegerField(default=0)
    terrace_price_30 = models.PositiveIntegerField(default=0)
    terrace_price_50 = models.PositiveIntegerField(default=0)
    terrace_price_100 = models.PositiveIntegerField(default=0)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True, related_name='room_details')

    @property
    def get_life_area(self):
        return self.full_area - self.terrace_area

    def __str__(self):
        return self.count_rooms
