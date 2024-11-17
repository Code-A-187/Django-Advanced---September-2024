from django.urls import path

from libraryApi.books import views

urlpatterns = [
    path('', views.index, name='index')
]