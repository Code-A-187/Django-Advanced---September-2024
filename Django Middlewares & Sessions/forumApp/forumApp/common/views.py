from pprint import pprint

from django.http import HttpResponse
from django.shortcuts import render


def view_counter(request):
    pprint(dict(request.session))
    request.session['counter'] = request.session.get('counter', 0) + 1

    return HttpResponse(f'The count is {request.session.get('counter')}')
