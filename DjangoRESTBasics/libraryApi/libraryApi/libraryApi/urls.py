
from django.contrib import admin
from django.urls import path, include

import libraryApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('libraryApi.books.urls')),
]
