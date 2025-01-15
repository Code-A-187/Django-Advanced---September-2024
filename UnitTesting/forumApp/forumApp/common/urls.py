from django.urls import path
from forumApp.common.views import view_counter, SetTimeCookie

urlpatterns = [
    path('count/', view_counter, name='counter'),
    path('last-visit/', SetTimeCookie.as_view(), name='set-time'),
]
