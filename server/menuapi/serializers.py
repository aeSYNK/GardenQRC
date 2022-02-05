from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


# class RoomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Room
#         fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=4, min_length=4, read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'token',)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=4, write_only=True)

    # Ignore these fields if they are included in the request.
    username = serializers.CharField(max_length=255)
    # username = serializers.CharField(max_length=255, read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        """
        Validates user data.
        """
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError(
                'An username is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return data

        # return {
        #     'token': user.token,
        # }

    # class RoomAuthSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = RoomAuthentication
    #         fields = '__all__'
