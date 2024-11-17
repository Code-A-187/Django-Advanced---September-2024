from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from libraryApi.books.models import Book
from libraryApi.books.serializers import BookSerializer

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
