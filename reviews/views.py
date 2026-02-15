from django.db.models import Avg
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from books.models import Book
from reviews.forms import ReviewForm
from reviews.models import Review



def book_reviews(request: HttpRequest, pk:int) -> HttpResponse:
    book = get_object_or_404(Book, pk=pk)
    reviews = book.reviews.all()

    average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0

    reviews_count = reviews.count()

    context = {'book': book,
               'reviews': reviews,
               'average_rating': average_rating,
               'reviews_count': reviews_count
               }

    return render(request, 'reviews/reviews-book.html', context)

# class ReviewCreateView(CreateView):
#     model = Review
#     form_class = ReviewForm
#     success_url = reverse_lazy('books:index')
#
#     def form_valid(self, form):
#         book = get_object_or_404(Book, pk=self.kwargs['pk'])
#         form.instance.book = book
#         return super().form_valid(form)


def create_review(request: HttpRequest, pk:int) -> HttpResponse:
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            return redirect('reviews:book-reviews', pk=book.pk)
    else:
        form = ReviewForm()

    context = {'book': book,
                   'form': form}
    return render(request, 'reviews/review-add.html', context)

def delete_review(request: HttpRequest, pk:int) -> HttpResponse:
    review = get_object_or_404(Review, pk=pk)
    book_id = review.book.id

    if request.method == 'POST':
        review.delete()
        return redirect('reviews:book-reviews', pk=book_id)

    context = {'review': review}

    return render(request, 'reviews/review-delete.html', context)

def edit_review(request: HttpRequest, pk:int) -> HttpResponse:
    review = get_object_or_404(Review, pk=pk)
    book_id = review.book.id

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviews:book-reviews', pk=book_id)
    else:
        form = ReviewForm(instance=review)

    context = {
        'form': form,
        'review': review,
    }

    return render(request, 'reviews/review-edit.html', context)

