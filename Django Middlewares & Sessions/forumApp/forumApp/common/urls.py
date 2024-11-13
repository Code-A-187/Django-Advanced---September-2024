from django.urls import path
from forumApp.common.views import view_counter

urlpatterns = [
    path('count/', view_counter, name='counter'),
]