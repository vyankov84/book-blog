from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from books.forms import AddBookForm
from books.models import Book


def index(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()

    context = {'books': books}
    return render(request, 'index.html', context)

class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/book-details.html'

def add_book(request: HttpRequest) -> HttpResponse:

    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:index')

    form = AddBookForm()
    context = {'form': form}
    return render(request, 'books/book-add.html', context)

def edit_book(request: HttpRequest, pk: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = AddBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books:index')
    else:
        form = AddBookForm(instance=book)

    context = {'form': form}
    return render(request, 'books/book-add.html', context)