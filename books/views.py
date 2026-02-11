from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from books.models import Book


def index(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()

    context = {'books': books}
    return render(request, 'index.html', context)

class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/book-details.html'
