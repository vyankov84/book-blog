from django.urls import path

from reviews import views

app_name = 'reviews'

urlpatterns = [
    path('<int:pk>/reviews/', views.book_reviews, name='book-reviews'),
    path('<int:pk>/add-review', views.create_review, name='add-review'),
    path('<int:pk>/delete-review/', views.delete_review, name='delete-review'),
    path('<int:pk>/edit-review/', views.edit_review, name='edit-review'),
]
