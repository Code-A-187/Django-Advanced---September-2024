from django.urls import path

from libraryApi.books import views
from libraryApi.books.views import ListBooksView

urlpatterns = [
    path('books/', ListBooksView.as_view(), name='list-books'),
    path('book/<int:pk>/', views.BookViewSet.as_view(), name='book_viewset'),
    path('publisher-links/', views.PublisherHyperlinkView.as_view(), name='publisher-link'),
    path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name='publisher-detail')
]