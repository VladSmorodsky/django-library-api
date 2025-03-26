from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from main.models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model
    """

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'genre']


class RegisterUserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model
    """
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(max_length=32, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=4, max_length=100, write_only=True)
    confirm_password = serializers.CharField(min_length=4, max_length=100, write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "confirm_password", "date_joined")

    def validate_username(self, value: str) -> str:
        """
        Validate username
        :param value:
        :return:
        """
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

    def validate(self, data: dict) -> dict:
        """
        Validate passwords
        :param data:
        :return:
        """
        password = data['password']
        confirmed_password = data['confirm_password']
        if password and confirmed_password and password != confirmed_password:
            raise serializers.ValidationError()
        return data

    def create(self, validated_data: dict) -> User:
        """
        Create and return a new `User` instance.
        :param validated_data:
        :return:
        """
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password(validated_data['password']))
        return user
