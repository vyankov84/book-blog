from django.core.validators import MinValueValidator
from django.db import models

from books.choices import BookGenreChoices
from books.validators import validate_isbn


class Book(models.Model):

    title = models.CharField(max_length = 100)

    author = models.CharField(max_length = 100)

    description = models.TextField()

    isbn_number = models.CharField(
        max_length = 20,
        validators = [validate_isbn],
        unique = True
    )

    genre = models.CharField(
        max_length = 30,
        choices = BookGenreChoices.choices,
    )

    publication_date = models.DateField()

    cover_image = models.URLField(
        max_length = 200,
        blank = True,
        null = True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators = [MinValueValidator(0)],
        default = 0,
    )


    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.author}'
