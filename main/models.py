from django.db import models


class Block(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Floor(models.Model):
    name = models.CharField(max_length=1234)
    block = models.ForeignKey(Block, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


STATUS = (
    ('пустой', 'пустой'),
    ('бронирование', 'бронирование'),
    ('продано', 'продано'),
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
    price_0 = models.PositiveIntegerField(default=0)
    price_30 = models.PositiveIntegerField(default=0)
    price_50 = models.PositiveIntegerField(default=0)
    price_100 = models.PositiveIntegerField(default=0)
    terrace_price_0 = models.PositiveIntegerField(default=0)
    terrace_price_30 = models.PositiveIntegerField(default=0)
    terrace_price_50 = models.PositiveIntegerField(default=0)
    terrace_price_100 = models.PositiveIntegerField(default=0)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True, related_name='room_details')

    @property
    def get_life_area(self):
        return self.full_area - self.terrace_area

    def __str__(self):
        return self.count_rooms

    # @property
    # def foiz_0(self):
    #     data = {
    #         'umumiy': ((self.price_0 * (
    #                 self.full_area - self.terrace_area) + self.terrace_price_0 * self.terrace_area) // 1000) * 1000,
    #         'oldindan_tolov': 0,
    #         'qolgan_summa': ((self.price_0 * (
    #                 self.full_area - self.terrace_area) + self.terrace_price_0 * self.terrace_area) // 1000) * 1000
    #     }
    #     return data

    # @property
    # def foiz_30(self):
    #     data = {
    #         'umumiy': ((self.price_30 * (
    #                 self.full_area - self.terrace_area) + self.terrace_price_30 * self.terrace_area) // 1000) * 1000,
    #         'oldindan_tolov': (self.price_30 * (
    #                 self.full_area - self.terrace_area) + self.terrace_price_30 * self.terrace_area) * 0.3,
    #         'qolgan_summa': (self.price_30 * (
    #                 self.full_area - self.terrace_area) + self.terrace_price_30 * self.terrace_area) * 0.7
    #     }
    #     return data

    # @property
    # def foiz_50(self):
    #     data = {
    #         'umumiy': ((self.price_50 * (
    #                 self.full_area - self.terrace_area) + self.terrace_price_50 * self.terrace_area) // 1000) * 1000,
    #         'oldindan_tolov': (self.price_50 * (
    #                 self.full_area - self.terrace_area) + self.terrace_price_50 * self.terrace_area) * 0.5,
    #         'qolgan_summa': (self.price_50 * (
    #                 self.full_area - self.terrace_area) + self.terrace_price_50 * self.terrace_area) * 0.5
    #     }
    #     return data

    # @property
    # def foiz_100(self):
    #     data = {
    #         'umumiy': ((self.price_50 * (
    #                 self.full_area - self.terrace_area) + self.terrace_price_100 * self.terrace_area) // 1000) * 1000,
    #         'oldindan_tolov': (self.price_50 * (
    #                 self.full_area - self.terrace_area) + self.terrace_price_100 * self.terrace_area),
    #         'qolgan_summa': 0
    #     }
    #     return data
