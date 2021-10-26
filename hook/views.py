from django.shortcuts import render
from django import template
from django.http import HttpResponse

# Create your views here.




# Create your views here.
def hook(request):
    return HttpResponse('Transaction successful')