from django.urls import path

from books import views
from books.views import DetailView

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/details', DetailView.as_view(), name='details'),
    path('add-book', views.add_book, name='book-add'),
    path('<int:pk>/edit-book', views.edit_book, name='book-edit'),
]
