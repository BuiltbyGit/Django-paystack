from django import template
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def paymentprocess(request):
    return render(request, 'paymentprocess/index.html', {'price': 1000})

    