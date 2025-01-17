from django.urls import path, include
from rest_framework.routers import DefaultRouter

from libraryApi.books import views
from libraryApi.books.views import ListBooksView, PublisherViewSet

router = DefaultRouter() # used for generating URLS dynamically
router.register('', PublisherViewSet)

urlpatterns = [
    path('books/', ListBooksView.as_view(), name='list-books'),
    path('book/<int:pk>/', views.BookViewSet.as_view(), name='book_viewset'),
    path('publisher-links/', views.PublisherHyperlinkView.as_view(), name='publisher-link'),
    path('publishers/', include(router.urls))
]