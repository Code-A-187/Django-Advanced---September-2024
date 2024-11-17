from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return JsonResponse({
        "name": "Anton"
    })


"""
Django MPA Server-Side rendering

books/               - Read List    - GET
book/<int:pk>/details- Read Details - GET
book/<int:pk>/create - Create       - GET/POST
book/<int:pk>/edit   - Update       - GET/POST
book/<int:pk>/delete - Delete       - GET/POST

---

Django REST

books/               - Read List    - GET
book/<int:pk>/       - Update, Create, Details, Delete, Partially update
                     - PUT,    POST  , GET    , DELETE, PATCH                       
"""

