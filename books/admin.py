from django.contrib import admin

from books import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'author',
        'description',
        'isbn_number',
        'genre',
        'publication_date',
        'created_at'
    ]

    search_fields = ['title', 'author', 'isbn_number']

    list_filter = ['genre', 'publication_date']