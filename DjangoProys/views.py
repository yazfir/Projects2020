"""
DjangoProys.Views
"""

#Django
from django.http import HttpResponse

#Utilities
from datetime import datetime
import json

def hello_word(request):
    """ Say Hello with Current Time"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')

    return HttpResponse(f'Hello, Current Server Time is {now}')


def read_params(request):
    """ Read params from URL """
    numbers=[int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    #Con esta línea se puede debbugear y consultar en la consola el valor de las variables, request, etc. hasta este punto. Letra 'c' para continuar.
    #import pdb; pdb.set_trace()
    data={
        'status':'ok',
        'numbers':sorted_ints,
        'message':'Integers sorted successfully.'
    }
    return HttpResponse(json.dumps(data,indent=4), content_type='application/json')

def difparams(request, name, age):
    """ Validate Age from Params """
    if age < 12:
        message = f'Sorry {name}, you are not allowed here.'
    else:
        message= f'Hello {name}, Welcome to Django Proys.'
    return HttpResponse(message)