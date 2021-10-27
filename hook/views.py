from django.shortcuts import render
from django import template
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.




# Create your views here.
@csrf_exempt
def hook(request):
    # return HttpResponse('Transaction successful')
    if request.is_ajax():
        if request.method == 'POST':
            print (request.body)   
            return HttpResponse(request.body)
    return HttpResponse('Okay')