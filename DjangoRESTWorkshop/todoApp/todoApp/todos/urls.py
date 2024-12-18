from django.urls import path

from todoApp.todos.views import TodoListCreateApiView

urlpatterns = [
    path('', TodoListCreateApiView.as_view(), name='todo-list-create'),
]