from django.db import models


# Create your models here.

class Book(models.Model):
    """
    Book model
    """
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.author.__str__()} - {self.title}'
