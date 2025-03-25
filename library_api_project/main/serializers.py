from rest_framework import serializers

from main.models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model
    """

    class Meta:
        model = Book
        fields = '__all__'
