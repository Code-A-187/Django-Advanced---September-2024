
from rest_framework.generics import ListCreateAPIView
from todoApp.todos.models import Todo
from todoApp.todos.serializers import TodoSerializer


class TodoListCreateApiView(ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        queryset = Todo.objects.all()

        category = self.request.query_params.get('category')
        is_done = self.request.query_params.get('is_done')

        if category:
            queryset = queryset.filter(category__name=category)

        if is_done:
            queryset = queryset.filter(state=is_done.lower() == 'true')

        return queryset

