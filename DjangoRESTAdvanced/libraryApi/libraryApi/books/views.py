from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, get_object_or_404, RetrieveAPIView, RetrieveUpdateDestroyAPIView, \
    ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from libraryApi.books.models import Book, Publisher
from libraryApi.books.permissions import IsBookOwner
from libraryApi.books.serializers import BookSerializer, PublisherHyperLinkSerializer, PublisherSerializer, \
    BookSimpleSerializer


# from django.http import JsonResponse
# from django.shortcuts import render
#
#
# def index(request):
#     return JsonResponse({
#         "name": "Anton"
#     })
#
#
# """
# Django MPA Server-Side rendering
#
# books/               - Read List    - GET
# book/<int:pk>/details- Read Details - GET
# book/<int:pk>/create - Create       - GET/POST
# book/<int:pk>/edit   - Update       - GET/POST
# book/<int:pk>/delete - Delete       - GET/POST
#
# ---
#
# Django REST
#
# books/               - Read List    - GET
# book/<int:pk>/       - Update, Create, Details, Delete, Partially update
#                      - PUT,    POST  , GET    , DELETE, PATCH
# """


# def list_books_view(request):
#     books = Books.objects.all()
#
#     context = {
#         'books': books,
#     }
#
#     return return(request, 'some_template.html')
#

# Option without REST framework
# def list_books_view(request):
#     books = Book.objects.all()
#
#     context = {
#         'books': books,
#     }
#
#     return JsonResponse(context) # TODO parse the context to JSON

# For next time Generic views
# class ListBooksApiView(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

@api_view(['GET', 'POST',])
def list_books_view(request):
    if request.method == 'GET':
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListBooksView(ListCreateAPIView):  # APIView is the base class same as View in Django
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class BookViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSimpleSerializer
    permission_classes = [IsAuthenticated, IsBookOwner]
    authentication_classes = [TokenAuthentication]


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherHyperlinkView(ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherHyperLinkSerializer

