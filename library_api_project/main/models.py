from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.db.models import DO_NOTHING


# Create your models here.

class Book(models.Model):
    """
    Book model
    """
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=DO_NOTHING)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.author.__str__()} - {self.title}'
