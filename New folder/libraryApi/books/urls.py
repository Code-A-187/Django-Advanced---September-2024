from django.urls import path

from libraryApi.books import views

urlpatterns = [
    path('books/', views.list_books_view, name='list-books'),
    path('book/<int:pk>/', views.BookViewSet.as_view(), name='book_viewset'),
]