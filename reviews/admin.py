from django.contrib import admin

from reviews import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = [
        'first_name',
        'last_name',
        'email',
        'rating',
        'book_title'
    ]

    def book_title(self, obj):
        return obj.book.title