from django.db import models


# Create your models here.

class Author(models.Model):
    """
    Author model
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Genre(models.Model):
    """
    Genre model
    """
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}'


class Book(models.Model):
    """
    Book model
    """
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, blank=True, null=True, on_delete=models.DO_NOTHING)
    publication_year = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.author.__str__()} - {self.title}'
