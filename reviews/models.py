from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from books.models import Book


class Review(models.Model):
    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    review_text = models.TextField()

    email = models.EmailField()

    age = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.book.title}'