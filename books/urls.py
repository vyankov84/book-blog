from django.urls import path

from books import views
from books.views import DetailView

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/details', DetailView.as_view(), name='details'),
]
