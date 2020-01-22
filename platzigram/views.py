from django.http import HttpResponse
from django.http import JsonResponse
import json
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    
    return HttpResponse('La hora es: {now}'.format(now=now))

def hola(request):
    numbers = request.GET['numbers'].split(',')
    numbers_sorted = list(map(int, numbers))
    numbers_sorted.sort()
    data = {
        'status' : 'Ok',
        'numbers': numbers_sorted,
        'message': 'Lista ordenada'
    }
    return JsonResponse(data)

def saluda(request, name, age):
    if age < 12:
        message = 'Sorry, you are too young'
    else:
        message ='Hi! Welcome'

    return HttpResponse(message)