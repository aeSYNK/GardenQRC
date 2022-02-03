from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Menu(models.Model):
    title = models.CharField('Название блюда', max_length=200)
    content = models.TextField('Описание блюда')
    weight = models.IntegerField('Вес блюда')
    image = models.ImageField(upload_to='dishes/')
    in_stock = models.BooleanField('В наличии', default=True)
    price = models.IntegerField('Цена', default=0)

    def __str__(self):
        return f"{self.title}"


class Order(models.Model):
    new_order = models.ForeignKey('Room', on_delete=models.DO_NOTHING)
    dish = models.ForeignKey(Menu, on_delete=models.DO_NOTHING)
    amount = models.IntegerField('Количество', validators=[MaxValueValidator(20), MinValueValidator(1)], default=0)
    order_date = models.DateTimeField('Время заказа')
    is_done = models.BooleanField('В процессе', default=False)

    def __str__(self):
        return f"{self.is_done}"


class Room(models.Model):
    pin_code = models.CharField('Пин-код', max_length=4)

    def __str__(self):
        return f"{self.pk}"