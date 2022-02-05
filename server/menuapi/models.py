    # Base
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
import qrcode
from .managers import *
    # User(AbstractBaseUser, PermissionsMixin)
# import jwt
# from django.conf import settings
# import datetime
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Номер комнаты', db_index=True, max_length=255, unique=True)
    # password = models.CharField(max_length=4, default=get_pin_code())
    qrcode = models.ImageField(upload_to='qr_codes/', blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ('username',)

    objects = UserManager()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        input_data = f"http://127.0.0.1:8000/room/{self.username}"
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(input_data)
        qr.make(fit=True)
        self.qrcode = qr.make_image(fill='black', back_color='white')
        self.qrcode.save(f'media/qrcode{self.username}.png')
        self.qrcode = f'qrcode{self.username}.png'
        self.save_base(self.qrcode)

    def __str__(self):
        return self.username

    # @property
    # def token(self):
    #     return self._generate_jwt_token()
    #
    # def _generate_jwt_token(self):
    #     # dt = datetime.now() + datetime.timedelta(days=1)
    #     token = jwt.encode({
    #         'id': self.pk,
    #         'exp': datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(seconds=30)
    #     }, settings.SECRET_KEY, algorithm='HS256')
    #     return token.decode('utf-8')


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
    # order_owner = models.ForeignKey('Room', on_delete=models.DO_NOTHING)
    order_owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    amount = models.IntegerField('Количество', validators=[MaxValueValidator(20), MinValueValidator(1)], default=0)
    order_date = models.DateTimeField('Время заказа')
    is_done = models.BooleanField('В процессе', default=False)

    def __str__(self):
        return f"{self.is_done}"


class OrderDetail(models.Model):
    dish = models.ForeignKey(Menu, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)


# class Room(models.Model):
#     pin_code = models.CharField('Пин-код', max_length=4, blank=True, default=get_pin_code())
#     qrcode = models.ImageField(upload_to='qr_codes/', blank=True)
#     room_number = models.IntegerField('Номер комнаты')
#
#     def __str__(self):
#         return f"{self.pk}"
#
#     def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
#         input_data = f"http://127.0.0.1:8000/room/{self.room_number}"
#         qr = qrcode.QRCode(
#             version=1,
#             box_size=10,
#             border=5)
#         qr.add_data(input_data)
#         qr.make(fit=True)
#         # print(self.__dict__)
#         self.qrcode = qr.make_image(fill='black', back_color='white')
#         self.qrcode.save(f'media/qrcode{self.room_number}.png')
#         self.qrcode = f'qrcode{self.room_number}.png'
#         self.save_base(self.qrcode)


# class RoomAuthentication(authentication.BaseAuthentication):
#     def authenticate(self, request):
#         username = request.META.get('HTTP_X_USERNAME')
#         if not username:
#             return None
#
#         try:
#             user = Room.objects.get(pk=username)
#         except User.DoesNotExist:
#             raise exceptions.AuthenticationFailed('No such user')
#
#         return (user, None)
