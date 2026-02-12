from django.urls import path

from books import views
from books.views import DetailView

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-book', views.add_book, name='book-add'),
    path('<int:pk>/details', DetailView.as_view(), name='details'),
    path('<int:pk>/edit-book', views.edit_book, name='book-edit'),
    path('<int:pk>/delete-book', views.delete_book, name='book-delete'),
]
